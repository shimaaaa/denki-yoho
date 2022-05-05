from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class DBSettingDefinition(BaseSettings):
    db_user: str
    db_pass: str
    db_name: str
    db_host: str
    db_port: int = 5432

    @property
    def connection_url(self):
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


DBSetting = DBSettingDefinition()
Engine = create_engine(
    DBSetting.connection_url,
    encoding="utf-8",
    echo=False,
)

ModelBase = declarative_base()
