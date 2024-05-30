from fastapi import FastAPI
from routes import user, inventory, auth
from database.db import db

app = FastAPI(debug=True)
db.connect(reuse_if_open=True)

@app.get('/')
def index():
    return {
        "message": "Hello, World"
    }

app.include_router(user.router, prefix="/user")
app.include_router(inventory.router, prefix="/inventory")
app.include_router(auth.router, prefix="/auth")