from fastapi import APIRouter, Request
from database.models import Users
import bcrypt
from database.db import db
from database.models import Users

router = APIRouter()

@router.post('/login')
async def index(req: Request):
    body = await req.json()

    get_user = Users.get(Users.username == body['username'])

    print(get_user)

    return {
        "path": "/auth/login",
        "captured_data": body['username']
    }