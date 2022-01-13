from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    """User Base schema for User model."""

    first_name: Optional[str]
    last_name: Optional[str]
    username: str
    email: str
    password: str
    phone_number: str

    class Config:
        orm_mode = True


class UserInputSchema(UserBaseSchema):
    """User Input schema for User model."""
    password: str


class UserOutputSchema(UserBaseSchema):
    """User Output schema for User model."""
    id: Union[UUID, int, str]
    is_active: bool
