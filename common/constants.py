import enum


class ApiVersion(enum.Enum):
    V1 = 1


# User model constants.
class UserModelConstants(enum.Enum):
    CHAR_SIZE_64 = 64
    CHAR_SIZE_128 = 128
    CHAR_SIZE_256 = 256
    TRUE = True
    FALSE = False
