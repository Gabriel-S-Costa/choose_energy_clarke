from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from .models import State, Supplier


class SupplierRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_suppliers(self, offset: int = 0, limit: int = 10) -> tuple[list[Supplier], int]:
        query = select(Supplier).options(selectinload(Supplier.states)).order_by(Supplier.name).offset(offset).limit(limit)
        result = self.session.exec(query)
        total = result.all()
        return total, len(total)

    def search_suppliers_by_state(self, state: str) -> tuple[State | None, list[Supplier]]:
        query = select(State).options(selectinload(State.suppliers)).filter(State.uf == state)
        state = self.session.exec(query).first()
        if not state:
            return None, []
        return state, state.suppliers
