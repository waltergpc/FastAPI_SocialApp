from fastapi import FastAPI
from .database import engine
from . import models
from .Routes import userRoutes, postRoutes, authRoutes, voteRoutes
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authRoutes.router)
app.include_router(postRoutes.router)
app.include_router(userRoutes.router)
app.include_router(voteRoutes.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
