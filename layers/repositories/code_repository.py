
from .base_repository import BaseRepository
from .models.code_model import Code

class CodeRepository(BaseRepository):
    def get_available_codes(self, limit=10) -> list:
        return (
            self.session.query(Code)
            .filter(Code.status == "AVAILABLE")
            .limit(limit)
            .all()
        )

    def get_codes_by_order_id(self, order_id: int) -> list:
        return self.session.query(Code).filter_by(order_id=order_id).all()

    def bulk_update_status(self, updates: list):
        for update in updates:
            code = self.session.query(Code).filter_by(id=update['id']).first()
            if code:
                code.order_id = update.get("order_id")
                code.status = update.get("status")
        self.session.commit()

    def create_code(self, code_value: str, status="AVAILABLE"):
        code = Code(code=code_value, status=status)
        self.session.add(code)
        self.session.commit()
        return code
