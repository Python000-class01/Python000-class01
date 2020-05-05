from . import db



class Tencentcomm(db.Model):
    __tablename__='tencentcomm'

    id=db.Column(db.Integer,nullable=True,primary_key=True,autoincrement=True)
    cmtid=db.Column(db.String)
    comment=db.Column(db.String)
    div_comment=db.Column(db.String)
    time=db.Column(db.String)
    sentiment=db.Column(db.String)
    sort_sentiment=db.Column(db.String)

