import math
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.shared.dependencies import get_supplier_service

from .filters import FilterSupplierParams
from .schemas import PaginatedSupplierResponse, SupplierResponse, SupplierSearchRequest
from .service import SupplierService

router = APIRouter(prefix='/suppliers', tags=['suppliers'])


@router.get('/', response_model=PaginatedSupplierResponse)
async def get_suppliers(filter_query: Annotated[FilterSupplierParams, Query()], supplier_service: SupplierService = Depends(get_supplier_service)):
    page = filter_query.page
    size = filter_query.size
    suppliers, total = supplier_service.get_all_suppliers(page=page, size=size)
    return {
        'items': suppliers,
        'total': total,
        'page': page,
        'size': size,
        'pages': math.ceil(total / size),
    }


@router.get('/search', response_model=list[SupplierResponse])
async def search_suppliers(search_query: Annotated[SupplierSearchRequest, Query()], supplier_service: SupplierService = Depends(get_supplier_service)):
    return supplier_service.search_suppliers(search_query)
