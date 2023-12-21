from fastapi import APIRouter

from schema import ResponseSchema, user_dep

question_router = APIRouter(prefix='/question', tags=['Question'])


@question_router.get('/{question_id}', response_model=ResponseSchema)
async def get_question_by_id(current_user: user_dep, question_id: str):
    return ResponseSchema(detail='Successfully fetch data!', result={question_id})


@question_router.get('/', response_model=ResponseSchema)
async def get_questions_by_theme(current_user: user_dep, theme: str):
    return ResponseSchema(detail='Successfully fetch data!', result=[theme])
