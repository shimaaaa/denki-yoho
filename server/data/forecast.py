from datetime import date, datetime

from helpers.constants import Area
from pydantic import BaseModel


class DemandForecast(BaseModel):
    area: Area
    dt: datetime
    actual_result: int
    forecast_demand: int
    forecast_supply: int


class PeakForecast(BaseModel):
    area: Area
    date: date
    hour_24: int
    max_demand_kw: int
    supply_kw: int


class DemandPeakForecast(PeakForecast):

    """

    需要ピーク時

    """

    pass


class UsagePeakForecast(PeakForecast):
    """

    使用率ピーク時

    """

    pass
