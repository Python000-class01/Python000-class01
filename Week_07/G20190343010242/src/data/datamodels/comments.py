from sqlalchemy import Column, BIGINT, Text, String, FLOAT, DATETIME
from datamodels.base_model import Base


class Comments(Base):
    __tablename__ = 'comments'

    comment_id = Column(BIGINT, primary_key=True, nullable=False)
    news_id = Column(String(32), index=True, nullable=False)
    comment = Column(Text, nullable=False)
    comment_time = Column(DATETIME, nullable=False)
    sentiment = Column(FLOAT, nullable=False)

