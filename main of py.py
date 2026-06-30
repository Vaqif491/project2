from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import user_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI basics task")
app.include_router(user_controller.router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}


# app/seed.py
import json
from pathlib import Path
from app.database import SessionLocal, engine
from app.models.users import User

Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()
    try:
        data = json.loads(Path("app/seed/data.json").read_text
        (encoding="utf-8"))

    finally:
        db.close()

    if __name__ == "__main__":
        seed_data()
