from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    Date,
    DateTime,
    Enum,
)
from sqlalchemy.schema import UniqueConstraint
from helpers.constants import Area, ForecastType
from .settings import ModelBase


class Forecast(ModelBase):
    """
    ForecastModel
    """

    __tablename__ = "forecast"
    __table_args__ = (UniqueConstraint("area", "forecast_type", "target_date"), {})

    id = Column(Integer, primary_key=True)
    area = Column(Enum(Area), nullable=False)
    forecast_type = Column(Enum(ForecastType), nullable=False)
    target_date = Column(Date, nullable=False)
    peak_hour_24 = Column(Integer, nullable=False)
    max_demand_kw = Column(Float, nullable=False)
    supply_kw = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
