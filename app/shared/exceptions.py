from app.core.base_exception import AppBaseException


class SupplierNotFoundException(AppBaseException):
    def __init__(self, detail: str = 'Fornecedor não encontrado'):
        super().__init__(detail, status_code=404)
