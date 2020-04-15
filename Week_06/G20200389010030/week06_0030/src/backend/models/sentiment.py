from sqlalchemy import Column, BIGINT, Integer, String, Text, FLOAT
from models.base_model import Base


class Sentiment(Base):
    __tablename__ = 'sentiment'

    item_id = Column(BIGINT, primary_key=True, nullable=False, autoincrement=True)
    item_name = Column(String(255), index=True, nullable=False)
    score = Column(Integer, nullable=False)
    trend = Column(String(255), nullable=False)
    comment = Column(Text, nullable=False)
    sentiment = Column(FLOAT, nullable=False)

    def to_dict(self):
        return {'item_id': self.item_id,
                'item_name': self.item_name,
                'score': self.score,
                'trend': self.trend,
                'comment': self.comment,
                'sentiment': self.sentiment
                }
