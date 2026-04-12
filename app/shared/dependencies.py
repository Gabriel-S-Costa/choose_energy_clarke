from fastapi import Depends, Header, HTTPException, status
from sqlmodel import Session

from app.core.config import settings
from app.core.database import db
from app.modules.suppliers.repository import SupplierRepository
from app.modules.suppliers.service import SupplierService
from app.shared.interfaces import ISupplierReporsitory


def get_supplier_repo(session: Session = Depends(db.get_session_conn)) -> ISupplierReporsitory:
    return SupplierRepository(session)


def get_supplier_service(repository: ISupplierReporsitory = Depends(get_supplier_repo)) -> SupplierService:
    return SupplierService(repository)


def verify_request_token(x_request_token: str = Header(alias='X-Request-Token')):
    if x_request_token != settings.ACCESS_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Header X-Request-Token is invalid or missing')
