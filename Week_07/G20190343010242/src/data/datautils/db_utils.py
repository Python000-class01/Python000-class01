import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event import listen


class DbUtils:

    def __init__(self):
        host = os.getenv("DB_ADDR")
        db = "newscomments"
        user = os.getenv("DB_USER")
        passwd = os.getenv("DB_PASS")
        charset = "utf8mb4"
        db_url = f"mysql+pymysql://{user}:{passwd}@{host}/{db}?charset={charset}"
        self.engine = create_engine(db_url, max_overflow=5, pool_size=5)
        self.Session = sessionmaker(bind=self.engine)

    def insert(self, objects):
        session = self.Session()
        session.add_all(objects)
        session.commit()
        session.close()

    def query(self, q, page=0, page_size=25):
        listen(q, 'before_compile', self.apply_limit(page, page_size), retval=True)
        return q

    def apply_limit(self, page, page_size):
        def wrapped(query):
            if page_size:
                query = query.limit(page_size)
                if page:
                    query = query.offset(page * page_size)
            return query
        return wrapped

