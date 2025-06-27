
from .base_repository import BaseRepository
from .models.order_model import Order

class OrderRepository(BaseRepository):
    def create_order(self, customer_id: int, dispense_type: str, order_received_date, number_of_codes: int, codes_send_date=None) -> int:
        order = Order(
            customer_id=customer_id,
            dispense_type=dispense_type,
            order_date=order_received_date,
            number_of_codes=number_of_codes,
            codes_send_date=codes_send_date
        )
        self.session.add(order)
        self.session.commit()
        return order.id

    def get_by_order_id(self, order_id: int) -> Order:
        return self.session.query(Order).filter_by(id=order_id).first()

    def get_by_customer_id(self, customer_id: int) -> list:
        return self.session.query(Order).filter_by(customer_id=customer_id).all()
