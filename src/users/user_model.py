from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

from user_enums.user_status import UserStatus
from user_enums.user_privileges import UserPrivilege

users = Table(
    "users",
    meta,
    Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
        ),
    Column(
        "first_name",
        String(255),
        nullable=True,
        ),
    Column(
        "last_name",
        String(255),
        nullable=True,
        ),
    Column(
        "user_name",
        String(255),
        nullable=False,
        unique=True,
        ),
    Column(
        "email",
        String(255),
        nullable=False,
        unique=True,
        ),
    Column(
        "password",
        String(255),
        nullable=False,
        ),
    Column(
        "user_status",
        UserStatus,
        nullable=False,
        ),
    Column(
        "user_privilege",
        UserPrivilege,
        nullable=False,
        ),
)

meta.create_all(engine)
