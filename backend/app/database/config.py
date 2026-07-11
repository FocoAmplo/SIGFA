from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:sigfabrasil@localhost:5432/sigfa"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
    echo=False,
)