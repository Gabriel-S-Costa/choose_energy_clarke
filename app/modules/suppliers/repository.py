import uuid

from sqlmodel import Session

from .models import Supplier


class SupplierRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_suppliers(self) -> list[Supplier]:
        return self.session.query(Supplier).all()

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
