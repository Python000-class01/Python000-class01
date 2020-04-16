from . import db

class Comment(db.Model):
    __tablename__='comment'

    id=db.Column(db.Integer,nullable=True,primary_key=True,autoincrement=True)
    content=db.Column(db.String)
    rating=db.Column(db.String)
    sentiment=db.Column(db.String)

    def __init__(self,content,rating,sentiment):
        self.content=content
        self.rating=rating
        self.sentiment=sentiment
