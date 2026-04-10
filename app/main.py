from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.base_exception import AppBaseException
from app.modules.suppliers.routes import router as suppliers_router

app = FastAPI()

app.include_router(suppliers_router)


@app.exception_handler(AppBaseException)
async def entity_error_handler(request: Request, exc: AppBaseException):
    return JSONResponse(
        content={'detail': exc.detail},
        status_code=exc.status_code,
    )


@app.get('/health-check')
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {'status': 'ok'}
