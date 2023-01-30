from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from . import models
# from .database import engine

from .routers import users, post, auth, vote
# from .config import settings


# DB
# models.Base.metadata.create_all(engine)


app = FastAPI(
        title='Social Media Demo',
        description='A simple social media for practice',
        version='0.0.1',
        contact={
            "name": 'Gustavo de los Santos',
            "email": 'gusleo94@gmail.com',
            },
        license_info={
            'name': "MIT"})


origins = [
    "http://localhost",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)
