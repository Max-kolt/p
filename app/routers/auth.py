from fastapi import APIRouter, Depends
from schema import RegisterSchema, ResponseSchema, TokenSchema
from services.auth import AuthService
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('/registration', response_model=ResponseSchema)
async def user_registration(request: RegisterSchema):
    token = await AuthService.register(request)
    return ResponseSchema(detail='Successfully save data!', result={"access_token": token, "token_type": "bearer"})


@auth_router.post('/token', response_model=TokenSchema)
async def user_login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = await AuthService.login(form)
    return TokenSchema(access_token=token, token_type='bearer')
