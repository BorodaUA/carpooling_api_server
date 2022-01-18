from fastapi import APIRouter, Depends

from auth.schemas import AuthUserInputSchema, AuthUserOutputSchema
from auth.services import AuthService
from users.schemas import UserOutputSchema

auth_router = APIRouter(prefix='/auth', tags=['Auth'])


@auth_router.post('/login', response_model=AuthUserOutputSchema)
async def login(
        user: AuthUserInputSchema,
        auth_service: AuthService = Depends(),
        ):
    """POST '/login' endpoint func, return auth header."""
    return await auth_service.login(user)


@auth_router.get('/me', response_model=UserOutputSchema)
async def auth_me(auth_service: AuthService = Depends()):
    """GET '/me' endpoint provides information about currently authenticated user."""
    return await auth_service.me()
