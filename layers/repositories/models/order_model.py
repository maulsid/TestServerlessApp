
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from layers.repositories.models.customer_model import Customer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(DateTime, nullable=False)
    dispense_type = Column(String, nullable=False)
    number_of_codes = Column(Integer, nullable=False)
    codes_send_date = Column(DateTime, nullable=True)

    customer = relationship("Customer")
