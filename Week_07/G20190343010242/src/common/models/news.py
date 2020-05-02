from sqlalchemy import Column, BIGINT, Integer, String, Text, FLOAT, DATETIME
from models.base_model import Base


class News(Base):
    __tablename__ = 'news'

    news_id = Column(String(32), primary_key=True, nullable=False)
    news_name = Column(String(500), nullable=False)
    source = Column(String(500), nullable=False)

    def to_dict(self):
        return {'news_id': self.news_id,
                'news_name': self.news_name,
                'source': self.source
                }
