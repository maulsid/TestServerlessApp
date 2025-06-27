
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Code(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    status = Column(String, nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    load_timestamp = Column(DateTime, nullable=False)
