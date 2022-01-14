import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


engine = create_async_engine(os.getenv('POSTGRES_DATABASE_URL'), echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False,
    )
    async with async_session() as session:
        yield session
