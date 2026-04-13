from typing import Protocol, runtime_checkable

from app.modules.suppliers.models import State, Supplier


@runtime_checkable
class ISupplierReporsitory(Protocol):
    def get_all_suppliers(self, offset: int = 0, limit: int = 10) -> tuple[list[Supplier], int]: ...

    def search_suppliers_by_state(self, state: str) -> tuple[State | None, list[Supplier]]: ...
