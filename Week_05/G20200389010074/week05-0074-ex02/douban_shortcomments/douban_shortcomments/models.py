from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine(
    'mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    rate = Column(String(64))
    comment = Column(String(2056))
    setiment = Column(String(20))


if __name__ == '__main__':
    Base.metadata.create_all(engine)