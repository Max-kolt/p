from fastapi import APIRouter

from schema import ResponseSchema, user_dep

quiz_router = APIRouter(prefix='/quiz', tags=['Quiz'])


@quiz_router.get('/{quiz_id}', response_model=ResponseSchema)
async def get_quiz_by_id(current_user: user_dep, quiz_id: str):
    return ResponseSchema(detail='Successfully fetch data!', result={quiz_id})

