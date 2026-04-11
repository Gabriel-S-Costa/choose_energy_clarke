from app.modules.suppliers.models import Supplier
from app.shared.interfaces import ISupplierReporsitory


class SupplierService:
    def __init__(self, reporitory: ISupplierReporsitory):
        self.reporitory = reporitory

    def get_all_suppliers(self, page: int = 1, size: int = 10) -> tuple[list[Supplier], int]:
        offset = (page - 1) * size
        return self.reporitory.get_all_suppliers(offset=offset, limit=size)

    def get_supplier_by_id(self, id: int) -> Supplier:
        return self.reporitory.get_supplier_by_id(id)
