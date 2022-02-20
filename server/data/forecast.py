from pydantic import BaseModel
from helpers.constants import Area


class PeakForecast(BaseModel):
    area: Area
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
