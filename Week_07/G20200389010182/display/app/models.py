# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, VARCHAR, TIMESTAMP, func
from sqlalchemy import Text
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

import click
from flask.cli import with_appcontext


from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def to_json(inst, cls):
	d = dict()
	for c in cls.__table__.columns:
		v = getattr(inst, c.name)
		d[c.name] = v
	return json.dumps(d)


from flask_login import UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.VARCHAR(32), nullable=False, unique=True)
    password_hash = db.Column(db.VARCHAR(128), nullable=False)

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True


class News(db.Model):
    __tablename__ = 'news'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ndesc = db.Column(db.Text)
    content_id = db.Column(db.VARCHAR(20), unique=True, nullable=False, index=True)
    event_time = db.Column(db.Integer)
    # collect_time = db.Column(db.TIMESTAMP, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    # collect_time = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
    # collect_time = db.Column(db.VARCHAR(16), nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    collect_time = db.Column(db.Float)
    event_date = db.Column(db.VARCHAR(10))

    @property
    def serialize(self):
        return to_json(self, self.__class__)


class Sentiments(db.Model):
    __tablename__ = 'sentiments'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    content_id = db.Column(db.ForeignKey('news.content_id'), unique=True)
    sentiment = db.Column(db.VARCHAR(20))
    content = db.relationship('News', primaryjoin='Sentiments.content_id == News.content_id', backref='sentiments')

    @property
    def serialize(self):
        return to_json(self, self.__class__)

def init_db():
    from config import Config
    from sqlalchemy import create_engine
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    from sqlalchemy.orm import sessionmaker
    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()

    User.__table__.create(engine, checkfirst=True)
    News.__table__.create(engine, checkfirst=True)
    Sentiments.__table__.create(engine, checkfirst=True)

    user1 = User(username='demo', password='demo')
    session.add_all([user1])
    session.commit()
    session.close()

@click.command("init-db")  
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")

if __name__ == "__main__":
    init_db()
