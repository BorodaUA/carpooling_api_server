import enum


class AuthJWTConstants(enum.Enum):
    """Auth JWT constants."""
    ALGORITHM_HS256 = 'HS256'
    ACCESS_TOKEN_TYPE = 'bearer'
    ACCESS_TOKEN_EXPIRE_60_MINUTES = 60
    REFRESH_TOKEN_EXPIRE_30_DAYS = 30
