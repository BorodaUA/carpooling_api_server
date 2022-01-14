from fastapi import FastAPI

from auth.routers import auth_router
from common.constants.api import ApiVersion
from users.routers import users_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router, prefix=f'/api/v{ApiVersion.V1.value}')
    app.include_router(auth_router, prefix=f'/api/v{ApiVersion.V1.value}')

    return app
