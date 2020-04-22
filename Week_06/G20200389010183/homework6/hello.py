from flask import Flask, render_template, redirect, url_for, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

app = Flask(__name__)


# 1. 完成从数据库读取数据 ok
# 2. 正确返回前台ok
# 3. 前段网页展示
# 4. 重构
#
class CommentDO(Base):
    # 表名
    __tablename__ = "jezt_comment_short"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    comment = Column(String(65535))
    rank = Column(Integer)
    sentiments = Column(Float)


@app.route('/post', methods=['post'])
def post():
    page_size = request.form['pageSize']
    return redirect(f"{url_for('hello_world')}?pageSize={page_size}")


@app.route('/')
def hello_world():
    star_to_number = {
        '5': '力荐',
        '4': '推荐',
        '3': '还行',
        '2': '较差',
        '1': '很差',
        '0': '很差'
    }
    page_size = 10
    if request.args.lists():
        page_size = request.args.to_dict().get('pageSize', 10)

    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8", echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # new_data = CommentDO(id=item['id'], rank=item['rank'], comment=item['comment'], sentiments=sent)
    res = session.query(CommentDO).order_by(CommentDO.sentiments.desc()).limit(page_size)
    lists = []
    for do in res:
        comment = {}
        comment["id"] = do.id
        comment["comment"] = do.comment
        comment["rank"] = do.rank
        print(do.sentiments)
        comment["sentiments"] = star_to_number[str(int(do.sentiments * 5))]
        lists.append(comment)

    # session.commit()
    return render_template('index.html', item_name='饥饿站台', results=lists)


if __name__ == '__main__':
    app.run(port=8080)
