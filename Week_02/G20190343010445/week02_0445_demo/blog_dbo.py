from flask_sqlalchemy import SQLAlchemy
import blog_models

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://python_train:python_train@localhost:3307/python_train"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'dev'

class DBConfig(object):
    db = SQLAlchemy()
    def __init__(self,app):
        app.config.from_object(Config)
        DBConfig.db.init_app(app)


class UserDBO(object):
    def __init__(self):
        pass

    def save_user(self,user):
        DBConfig.db.session.add(user);
        DBConfig.db.session.commit()
    
    def get_byname(self,username):
        return blog_models.BlogUser.query.filter_by(username=username).first()
    def validate_user(self,username,password):
        print('password:', password)
        return blog_models.BlogUser.query.filter_by(username=username,password=password).first()
    def get_byid(self,id):
        return blog_models.BlogUser.query.get(id)

class PostDBO(object):
    def __init__(self):
        pass
    def save_post(self,post):
        if post.id is None:
            DBConfig.db.session.add(post);
        else:
            post1 = DBConfig.db.session.query(blog_models.BlogPost).get(post.id)
            # post1 = self.get_byid(post.id)
            post1.title = post.title
            post1.body = post.body
            # DBConfig.db.session.update()
        
        DBConfig.db.session.commit()
        
    def get_all(self):
        return blog_models.BlogPost.query.all()

    def get_byid(self,id):
        return blog_models.BlogPost.query.get(id)

    def validate_post_author(self, userid, postid):
        return blog_models.BlogPost.query.filter_by(id= postid, author_id=userid).first()

    def delete_post(self,post):
        DBConfig.db.session.delete(post)
        DBConfig.db.session.commit()
