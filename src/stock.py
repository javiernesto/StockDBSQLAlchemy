import sqlalchemy
from base import Base


class Stock(Base):
    __tablename__ = 'stock'
    symbol = sqlalchemy.Column(sqlalchemy.String(10), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    sector = sqlalchemy.Column(sqlalchemy.String(50))
    sp_500 = sqlalchemy.Column(sqlalchemy.Boolean)
    
    
    def __init__(self, symbol=None, name=None, sector=None, sp_500=None):
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.sp_500 = sp_500
        