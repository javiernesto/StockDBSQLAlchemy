import sqlalchemy
from base import Base


class Config(Base):
    __tablename__ = 'config'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('config_id_seq'), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    value = sqlalchemy.Column(sqlalchemy.String(50))
