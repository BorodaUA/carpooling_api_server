import abc

from fastapi import Depends, status

from fastapi_jwt_auth import AuthJWT
from passlib.hash import argon2
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import AuthUserInputSchema
from auth.utils.exceptions import AuthUserInvalidPasswordException
from db import get_session
from users.services import UserService
from utils.logging import setup_logging


class AbstractAuthService(metaclass=abc.ABCMeta):

    def __init__(
        self,
        session: AsyncSession = Depends(get_session),
        Authorize: AuthJWT = Depends(),
    ) -> None:
        self._log = setup_logging(self.__class__.__name__)
        self.session = session
        self.user_service = UserService(session=self.session)
        self.Authorize = Authorize

    async def login(self, user: AuthUserInputSchema) -> None:
        """Login user with credentials."""
        return await self._login(user)

    async def me(self) -> None:
        """Return currently authenticated user."""
        return await self._me()

    async def verify_password(self, password: str, password_hash: str) -> bool:
        """Return bool of verifying password with argon2 algorithm."""
        return await self._verify_password(password, password_hash)

    @abc.abstractclassmethod
    async def _login(user: AuthUserInputSchema) -> None:
        pass

    @abc.abstractclassmethod
    async def _verify_password(self, password: str, password_hash: str) -> None:
        pass

    @abc.abstractclassmethod
    async def _me(self):
        pass


class AuthService(AbstractAuthService):

    async def _verify_password(self, password: str, password_hash: str) -> bool:
        return argon2.verify(password, password_hash)

    async def _login(self, user: AuthUserInputSchema) -> None:
        db_user = await self.user_service.get_user_by_username(username=user.username)
        if await self.verify_password(password=user.password, password_hash=db_user.password):
            access_token = self.Authorize.create_access_token(subject=user.username)
            refresh_token = self.Authorize.create_refresh_token(subject=user.username)

            self.Authorize.set_access_cookies(access_token)
            self.Authorize.set_refresh_cookies(refresh_token)
            return {'access_token': access_token, 'refresh_token': refresh_token}
        raise AuthUserInvalidPasswordException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorect username or password.',
            )

    async def _me(self) -> None:
        self.Authorize.jwt_required()
        current_user = self.Authorize.get_jwt_subject()
        user = await self.user_service.get_user_by_username(current_user)
        return user
