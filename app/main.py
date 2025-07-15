from .databases import SessionLocal
from fastapi import FastAPI
from app.endpoints import router  # si tu utilises APIRouter
from app.databases import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

# pour brancher tes endpoints
app.include_router(router)

