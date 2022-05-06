from helpers.constants import Area
from helpers.datetime import now, timezone
from sqlalchemy import Column, DateTime, Enum, Integer, TypeDecorator
from sqlalchemy.schema import UniqueConstraint

from .settings import ModelBase


class LocalDateTime(TypeDecorator):
    impl = DateTime

    def process_result_value(self, value, dialect):
        return value.astimezone(tz=timezone())


class DemandForecast(ModelBase):
    """
    DemandForecastModel
    """

    __tablename__ = "demand_forecast"
    __table_args__ = (UniqueConstraint("area", "dt"), {})

    id = Column(Integer, primary_key=True)
    area = Column(Enum(Area, name="demand_forecast_area", create_type=False), nullable=False)
    dt = Column(DateTime, nullable=False)
    actual_result = Column(Integer, nullable=False)
    forecast_demand = Column(Integer, nullable=False)
    forecast_supply = Column(Integer, nullable=False)
    created_at = Column(LocalDateTime, default=now, nullable=False)
    updated_at = Column(LocalDateTime, default=now, onupdate=now, nullable=False)
