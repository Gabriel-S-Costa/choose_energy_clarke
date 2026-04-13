import uuid

from pydantic import BaseModel, ConfigDict, field_validator


class SupplierResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    code: uuid.UUID
    name: str
    type: str
    total_clients: int
    avg_rating: float
    is_active: bool
    states: list[str]

    @field_validator('states', mode='before')
    @classmethod
    def transform_states(cls, value):
        if isinstance(value, list):
            return [getattr(state, 'uf', state) for state in value]
        return value


class PaginatedSupplierResponse(BaseModel):
    items: list[SupplierResponse]
    total: int
    page: int
    size: int
    pages: int


class SupplierSearchRequest(BaseModel):
    state: str
    consumption: int


class SupplierOfferResponse(BaseModel):
    type: str
    kwl_cost: int
    estimated_cost: int
    estimated_savings: int
    percentage_savings: float


class SupplierSearchItemResponse(SupplierResponse):
    offers: list[SupplierOfferResponse]


class SupplierSearchResultResponse(BaseModel):
    state_base_cost: int
    available_types: list[str]
    estimated_savings_per_type: dict[str, int]
    suppliers: list[SupplierSearchItemResponse]
