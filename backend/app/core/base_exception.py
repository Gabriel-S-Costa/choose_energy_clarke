class AppBaseException(Exception):
    def __init__(self, detail: str, status_code: int = 400):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)
