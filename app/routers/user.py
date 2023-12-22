

from fastapi import APIRouter

from schema import ResponseSchema, user_dep
from repository.users import UserRepository

user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.get('/{username}', response_model=ResponseSchema)
async def get_user_by_username(current_user: user_dep, username: str):
    user_info = await UserRepository().get_by_username_or_email(username=username)
    return ResponseSchema(detail='Successfully fetch data!', result={user_info})


@user_router.get('/get_all', response_model=ResponseSchema)
async def get_top_10_users(current_user: user_dep):
    users = await UserRepository.get_all()
    return ResponseSchema(detail='Successfully fetch data!', result=users)
