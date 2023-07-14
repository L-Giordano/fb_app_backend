from sqlalchemy import create_engine, MetaData

from config.env import (
    FBOOKING_DB_HOST,
    FBOOKING_DB_NAME,
    FBOOKING_DB_PASSWORD,
    FBOOKING_DB_PORT,
    FBOOKING_DB_USER,
)

engine = create_engine(
    f'mysql+pymysql://{FBOOKING_DB_USER}:{FBOOKING_DB_PASSWORD}' +
    f'@{FBOOKING_DB_HOST}:{FBOOKING_DB_PORT}/{FBOOKING_DB_NAME}'
    )

meta = MetaData()

conn = engine.connect()
