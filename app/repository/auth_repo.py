from config import SECRET_AUTH_KEY, ALGORITHM, EXPIRE_DELTA_TOKEN_MINUTES
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from fastapi import HTTPException, Request, Depends
from typing import Annotated
from datetime import datetime, timedelta


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class AuthRepository:
    @staticmethod
    async def create_token(data: dict) -> str:
        to_encode = data.copy()
        to_encode['exp'] = datetime.utcnow()+timedelta(minutes=EXPIRE_DELTA_TOKEN_MINUTES)
        return jwt.encode(to_encode, SECRET_AUTH_KEY, algorithm=ALGORITHM)

    @staticmethod
    async def decode_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_AUTH_KEY, algorithms=[ALGORITHM])
            return payload if payload['exp'] >= int(datetime.now().timestamp()) else None
        except Exception:
            raise Exception


async def verify_token(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = await AuthRepository.decode_token(token)

        username: str = payload.get('username')
        if username is None:
            raise HTTPException(status_code=401, detail='Could not validate user.')
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')

