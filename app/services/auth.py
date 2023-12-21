from schema import RegisterSchema, TokenSchema
from db import get_table, get_async_session
from passlib.context import CryptContext
from repository import AuthRepository, UserRepository
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class AuthService:
    @staticmethod
    async def register(register: RegisterSchema)->str:
        verify = await UserRepository().get_by_username_or_email(username=register.username)
        if verify:
            raise HTTPException(status_code=400, detail='Ussername already taken')

        model = RegisterSchema(
            username=register.username,
            email=register.email,
            password=bcrypt_context.hash(register.password)
        )
        await UserRepository().create(**model.model_dump())

        token = await AuthRepository.create_token(data={
            'username': register.username,
            'exp': datetime.utcnow()+timedelta(minutes=10)
        })
        return token

    @staticmethod
    async def login(login: OAuth2PasswordRequestForm) -> str:
        user = await UserRepository().get_by_username_or_email(email=login.username)
        if user:
            if bcrypt_context.verify(login.password, user.password):
                token = await AuthRepository.create_token(data={
                    'username': user.username,
                    'exp': datetime.utcnow() + timedelta(hours=24)
                })
                return token
        raise HTTPException(status_code=400, detail='Email or password not valid')



