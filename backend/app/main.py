from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.base_exception import AppBaseException
from app.modules.suppliers.routes import router as suppliers_router

app = FastAPI()

app.include_router(suppliers_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
