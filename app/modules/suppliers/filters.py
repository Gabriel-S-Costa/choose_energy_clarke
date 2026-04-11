from pydantic import BaseModel, Field


class FilterSupplierParams(BaseModel):
    page: int = Field(1, ge=1)
    size: int = Field(10, gt=0, le=100)
