from fastapi import FastAPI

from common.constants import ApiVersion
from users.routers import users_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router, prefix=f'/api/v{ApiVersion.V1.value}')

    return app
