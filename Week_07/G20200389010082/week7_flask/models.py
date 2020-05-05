from app import db


class BooKComments(db.Model):
    __tablename__ = 'news_comments'
    id = db.Column(db.Integer, primary_key=True)
    col_comment = db.Column(db.Text)
    col_sentiments = db.Column(db.String(512), index=True, unique=True)
    col_title = db.Column(db.String(255))
    col_time = db.Column(db.DateTime)
    col_link = db.Column(db.String(255))
    col_today = db.Column(db.DateTime)

    def __repr__(self):
        return '<Id {}>'.format(self.id)