
from .base_repository import BaseRepository
from .models.customer_model import Customer

class CustomerRepository(BaseRepository):
    def get_by_name(self, name: str) -> Customer:
        return self.session.query(Customer).filter_by(name=name).first()

    def create_customer(self, name: str, customer_type: str) -> Customer:
        customer = Customer(name=name, customer_type=customer_type)
        self.session.add(customer)
        self.session.commit()
        return customer

    def list_customers(self) -> list:
        return self.session.query(Customer).all()
