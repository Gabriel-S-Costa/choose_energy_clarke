import uuid

from app.modules.suppliers.models import Supplier
from app.shared.interfaces import ISupplierReporsitory


class SupplierService:
    def __init__(self, reporitory: ISupplierReporsitory):
        self.reporitory = reporitory

    def get_all_suppliers(self) -> list[Supplier]:
        return self.reporitory.get_all_suppliers()

    def get_supplier_by_id(self, id: int) -> Supplier:
        return self.reporitory.get_supplier_by_id(id)

    def get_supplier_by_code(self, code: uuid.UUID) -> Supplier:
        return self.reporitory.get_supplier_by_code(code)

    def create_supplier(self, supplier: Supplier) -> Supplier:
        return self.reporitory.create_supplier(supplier)

    def update_supplier(self, supplier: Supplier) -> Supplier:
        return self.reporitory.update_supplier(supplier)

    def delete_supplier(self, supplier: Supplier) -> None:
        self.reporitory.delete_supplier(supplier)
