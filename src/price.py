import sqlalchemy
from base import Base


class Price(Base):
    __tablename__ = 'price'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('price_id_seq'), primary_key=True)
    day = sqlalchemy.Column(sqlalchemy.DateTime)
    symbol = sqlalchemy.Column(sqlalchemy.String(10))
    open = sqlalchemy.Column(sqlalchemy.Float)
    close = sqlalchemy.Column(sqlalchemy.Float)
    high = sqlalchemy.Column(sqlalchemy.Float)
    low = sqlalchemy.Column(sqlalchemy.Float)
    volume = sqlalchemy.Column(sqlalchemy.Float)
    trade_count = sqlalchemy.Column(sqlalchemy.Integer)
    vwap = sqlalchemy.Column(sqlalchemy.Float)

    def __init__(self, day=None, symbol=None, open_price=None, close=None, high=None, low=None, volume=None,
                 trade_count=None, vwap=None):
        self.day = day
        self.symbol = symbol
        self.open = open_price
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.trade_count = trade_count
        self.vwap = vwap
