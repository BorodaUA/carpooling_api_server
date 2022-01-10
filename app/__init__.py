from fastapi import FastAPI
from hello_world import hello_world_router

def create_app():
    app = FastAPI()
    app.include_router(hello_world_router)
    return app
