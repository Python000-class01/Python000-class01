from utils.db_helper import DbHelper
from models.sentiment import Sentiment
import os
from pathlib import Path
import pandas as pd
from snownlp import SnowNLP


class SentimentService:

    def __init__(self):
        self.db_helper = DbHelper()

    def __init_data(self):
        session = self.db_helper.Session()
        query = session.query(Sentiment)
        ret = self.db_helper.query(query, page_size=1).count()
        if ret == 0:
            print("No data found, loading data...")
            # insert data
            items = []
            for data_item in self.__load_data():
                item_name = '嫌疑人'
                sentiment = self.__sentiment(data_item['comment'])
                item = Sentiment(item_name=item_name, score=data_item['score'], trend=data_item['trend'], comment=data_item['comment'], sentiment=sentiment)
                items.append(item)
            session.add_all(items)
            session.commit()
        session.close()

    def top_sentiments(self, page_size=10):
        self.__init_data()
        session = self.db_helper.Session()
        query = session.query(Sentiment).filter(Sentiment.sentiment < 0.99).order_by(Sentiment.sentiment.desc())
        results = self.db_helper.query(query, page_size=page_size)
        session.close()
        return [result.to_dict() for result in results]

    def __sentiment(self, text):
        return SnowNLP(text).sentiments

    def __load_data(self):
        backend_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
        source = backend_dir.joinpath("resources/data.csv")
        df = pd.read_csv(source)
        return df.to_dict('records')

