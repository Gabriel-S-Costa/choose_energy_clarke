import uuid
from datetime import datetime, timezone

from sqlmodel import Field, Relationship, SQLModel


class SupplierStateLink(SQLModel, table=True):
    __tablename__ = 'supplier_state'

    supplier_id: int = Field(foreign_key='supplier.id', primary_key=True)
    state_id: int = Field(foreign_key='state.id', primary_key=True)


class Supplier(SQLModel, table=True):
    __tablename__ = 'supplier'

    id: int | None = Field(primary_key=True, default=None)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = Field(default=None)
    name: str = Field(index=True, nullable=False)
    banner: str | None = Field(default=None)
    type: str | None = Field(default=None)
    kwl_cost: int = Field(default=0, nullable=False)
    total_clients: int = Field(default=0)
    avg_rating: float = Field(default=0.0)
    is_active: bool = Field(default=True)
    states: list['State'] = Relationship(back_populates='suppliers', link_model=SupplierStateLink)


class State(SQLModel, table=True):
    __tablename__ = 'state'

    id: int | None = Field(primary_key=True, default=None)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = Field(default=None)
    name: str = Field(nullable=False)
    uf: str = Field(index=True, nullable=False)
    base_cost_per_kwl: int = Field(default=0, nullable=False)
    suppliers: list['Supplier'] = Relationship(back_populates='states', link_model=SupplierStateLink)
