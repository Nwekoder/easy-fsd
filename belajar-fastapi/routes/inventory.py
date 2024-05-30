from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def index():
    return {
        "path": "/inventory"
    }

@router.get('/view/{uid}')
def view(uid:str):
    return {
        "path": f"/inventory/view/{uid}" 
    }