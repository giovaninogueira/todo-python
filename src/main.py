from dotenv import load_dotenv
from fastapi import FastAPI
from config.engine import engine
from models.user import Base
from routes import users_router, auth_router, tasks_router

load_dotenv()
app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(tasks_router)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["root"])
def red_root():
    return {"message": "Welcome to the Todo API!"}
