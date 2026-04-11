from fastapi import Depends
from sqlmodel import Session

from app.core.database import db
from app.modules.suppliers.repository import SupplierRepository
from app.modules.suppliers.service import SupplierService
from app.shared.interfaces import ISupplierReporsitory


def get_supplier_repo(session: Session = Depends(db.get_session_conn)) -> ISupplierReporsitory:
    return SupplierRepository(session)


def get_supplier_service(repository: ISupplierReporsitory = Depends(get_supplier_repo)) -> SupplierService:
    return SupplierService(repository)
