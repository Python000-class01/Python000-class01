from sqlalchemy import create_engine
from snownlp import SnowNLP

engine = create_engine(
        "mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4", 
        echo=True)
# echo=True：用于显示SQLAlchemy在操作数据库时所执行的SQL语句情况，
# 相当于一个监视器，可以清楚知道执行情况。

############ 创建数据表
from sqlalchemy import Column, Integer, String, DateTime 
# 常用数据类型

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Mytable(Base):
    # 表名
    __tablename__ ="bookcomm"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    grade = Column(String(25))
    evaluate = Column(String(10))
    shortcomm = Column(String)

Base.metadata.create_all(engine)

############## 删除表
#Base.metadata.drop_all(engine)

str_evaluate = ['1','2','3','4','5','6','7','8','9','10']
# 添加数据，创建一个会话对象，用于执行SQL语句
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind = engine)
session = DBSession()

get_data = session.query(Mytable).all()
totalcount = 0
totalevaluates = 0
for i in get_data:
    #print(f'id:{i.id}')
    #print(f'评论:{i.shortcomm}')
    s = SnowNLP(i.shortcomm)
    get_data2 = session.query(Mytable).filter_by(id=i.id).first()
    get_data2.grade = str(s.sentiments)
    if s.sentiments >= 1:
        get_data2.evaluate = str_evaluate[9]
    else:
        get_data2.evaluate = str_evaluate[int(s.sentiments * 10)]
    totalcount = totalcount + 1
    totalevaluates = totalevaluates + int(get_data2.evaluate)

    #if s.sentiments > 1:
    #   print(f'id:{i.id}')
    #    print(f'评论:{i.shortcomm}')
    #    print(f'评论:{s.sentiments}')

session.commit()
session.close()

print(f'推荐分数（10分满分）: {totalevaluates/totalcount}')