from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine(
    "postgresql://user:denkidb@localhost:5432/denkidb",
    encoding="utf-8",
    echo=False,
)

ModelBase = declarative_base()
