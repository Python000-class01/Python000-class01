import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db():
    """
    连接到应用程序配置的数据库。连接对于每个请求都是唯一的，如果调用再一次。
    """
    # g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
    if "db" not in g:
        # 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。这个文件现在还没有建立，后面会在初始化数据库的时候建立该文件。
        g.db = sqlite3.connect(
            # current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。这里 使用了应用工厂，那么在其余的代码中就不会出现应用对象。当应用创建后，在处理 一个请求时， get_db 会被调用。这样就需要使用 current_app 。
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # 告诉连接返回类似于字典的行，这样可以通过列名称来操作 数据。

    return g.db

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    """
    通过检查 g.db 来确定连接是否已经建立。如果连接已建立，那么就关闭连接。
    以后会在应用工厂中告诉应用 close_db 函数，这样每次请求后就会调用它。
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """清除现有数据并创建新表。"""
    db = get_db()

    # 打开一个文件，该文件名是相对于 flaskr 包的。这样就不需要考虑以后应用具体部署在哪个位置。 get_db 返回一个数据库连接，用于执行文件中的命令。
    with current_app.open_resource("schema.sql") as f:
        # 定义一个名为 init-db 命令行，它调用 init_db 函数，并为用户显示一个成功的消息。 更多关于如何写命令行的内容请参阅 ref:cli 。
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
@with_appcontext
def init_db_command():
    """清除现有数据并创建新表。"""
    init_db()
    click.echo("Initialized the database.")


# 在应用中注册
def init_app(app):
    """注册数据库功能到 Flask app.
    This is called by the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)