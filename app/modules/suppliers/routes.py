from fastapi import APIRouter

router = APIRouter(prefix='/suppliers', tags=['suppliers'])


@router.get('/search')
async def get_suppliers():
    return {'message': 'List of suppliers'}
