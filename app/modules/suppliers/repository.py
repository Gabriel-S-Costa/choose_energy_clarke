import uuid

from sqlalchemy.orm import selectinload
from sqlmodel import Session

from .models import Supplier


class SupplierRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_suppliers(self, offset: int = 0, limit: int = 10) -> tuple[list[Supplier], int]:
        query = self.session.query(Supplier).options(selectinload(Supplier.states))
        total = query.count()
        items = query.offset(offset).limit(limit).all()
        return items, total

    def get_supplier_by_id(self, id: int) -> Supplier:
        return self.session.query(Supplier).filter(Supplier.id == id).first()

    def get_supplier_by_code(self, code: uuid.UUID) -> Supplier:
        return self.session.query(Supplier).filter(Supplier.code == code).first()

    def create_supplier(self, supplier: Supplier) -> Supplier:
        self.session.add(supplier)
        self.session.commit()
        self.session.refresh(supplier)
        return supplier

    def update_supplier(self, supplier: Supplier) -> Supplier:
        self.session.add(supplier)
        self.session.commit()
        self.session.refresh(supplier)
        return supplier

    def delete_supplier(self, supplier: Supplier) -> None:
        self.session.delete(supplier)
        self.session.commit()
