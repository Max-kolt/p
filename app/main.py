from fastapi import FastAPI
from routers import all_routers
from config import APP_NAME
from db import load_db

app = FastAPI(title=APP_NAME)

for router in all_routers:
    app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await load_db()


@app.get('/')
async def host():
    return {'message': 'hello world!'}


