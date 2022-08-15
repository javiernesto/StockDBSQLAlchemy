import pandas as pd
import base
from sqlalchemy import create_engine, select
from stock import Stock
from price import Price
from config import Config


class StockModel(object):
    db_config = ''
    engine = object

    def __init__(self):
        self.engine = create_engine('sqlite+pysqlite:///stock.db')
        with self.engine.begin() as conn:
            base.Base.metadata.create_all(conn)

    def get_query_result(self, query):
        with self.engine.begin() as conn:
            return conn.execute(query).fetchall()

    """
    Stock Table
    """

    def get_all_stocks(self):
        data = self.get_query_result(select(Stock))
        df_stock = pd.DataFrame(data, columns=['symbol', 'name', 'sector', 'sp_500'])
        return df_stock