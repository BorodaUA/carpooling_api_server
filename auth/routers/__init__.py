from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import AuthUserInputSchema
from auth.services import AuthService
from db import get_session

auth_router = APIRouter(prefix='/auth', tags=['Auth'])


@auth_router.post('/login')
async def login(user: AuthUserInputSchema, session: AsyncSession = Depends(get_session)):
    """POST '/login' endpoint func, return auth header."""
    return await AuthService(session=session).login(user)
