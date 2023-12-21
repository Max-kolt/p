from fastapi import APIRouter
from schema import ResponseSchema

theme_router = APIRouter(prefix='/theme', tags=['User'])


@theme_router.get('/{theme_id}', response_model=ResponseSchema)
async def get_theme_by_id(theme_id: str):
    return ResponseSchema(detail='Successfully fetch data!', result={theme_id})
