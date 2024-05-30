from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def index():
    return {
        "path": "/user"
    }

@router.get('/view/{uid}')
def view(uid:str):
    return {
        "path": f"/user/view/{uid}" 
    }