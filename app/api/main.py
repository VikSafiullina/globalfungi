import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.data.models import Sample
from db.connector import DatabaseConnector
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.info")
db_connector = DatabaseConnector()

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = db_connector.get_session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


async def get_context(request: Request):
    return {
        "session": request.state.db,
        "logger": logger,
    }


@app.get("/dummy_sample")
async def get_dummy_sample(request: Request):
    response = None
    try:
        db = request.state.db
        dummy_sample = db.query(Sample).first(Sample.id==uuid.as_uuid("31b06e5f-a59a-4993-addd-000f9f09fb60"))

        return dummy_sample
    
    except Exception as e:
        logger.error(f"Error {e}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
