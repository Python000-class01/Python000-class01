from app import db


class BooKComments(db.Model):
    __tablename__ = 'book_comments'
    id = db.Column(db.Integer, primary_key=True)
    col_comment = db.Column(db.Text)
    col_sentiments = db.Column(db.String(512), index=True, unique=True)
    col_start_title= db.Column(db.String(20))

    def __repr__(self):
        return '<Id {}>'.format(self.id)