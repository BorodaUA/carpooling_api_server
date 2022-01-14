import abc

from passlib.hash import argon2
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import AuthUserInputSchema
from users.services import UserService
from utils.logging import setup_logging


class AbstractAuthService(metaclass=abc.ABCMeta):

    def __init__(self, session: AsyncSession) -> None:
        self._log = setup_logging(self.__class__.__name__)
        self.session = session
        self.user_service = UserService(session=self.session)

    async def login(self, user: AuthUserInputSchema) -> None:
        """Login user with credentials."""
        return await self._login(user)

    async def verify_password(self, password: str, password_hash: str) -> bool:
        """Return bool of verifying password with argon2 algorithm."""
        return await self._verify_password(password, password_hash)

    @abc.abstractclassmethod
    async def _login(user: AuthUserInputSchema) -> None:
        pass

    @abc.abstractclassmethod
    async def _verify_password(self, password: str, password_hash: str) -> None:
        pass


class AuthService(AbstractAuthService):

    async def _verify_password(self, password: str, password_hash: str) -> bool:
        return argon2.verify(password, password_hash)

    async def _login(self, user: AuthUserInputSchema) -> None:
        db_user = await self.user_service.get_user_by_username(username=user.username)
        if await self.verify_password(password=user.password, password_hash=db_user.password):
            # TODO: JWT logic here:
            return 'VALID PASS '
        return 'WRONG PASS'
