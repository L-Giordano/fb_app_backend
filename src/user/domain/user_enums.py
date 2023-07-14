from enum import Enum


class UserStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ARCHIVED = 'archived'


class UserPrivilege(Enum):
    USER = 'user'
    ADMIN = 'admin'
