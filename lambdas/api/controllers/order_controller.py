from litestar.controller import Controller
from litestar import get, post

class OrderController(Controller):
    path = "/admin/orders"

    @get()
    async def list_orders(self) -> dict:
        return {"orders": ["order1", "order2"]}

    @post()
    async def create_order(self, data: dict) -> dict:
        return {"message": "Order created", "data": data}