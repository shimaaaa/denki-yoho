from datetime import datetime
from typing import List

from helpers.constants import Area
from pydantic import BaseModel


class DemandForecast(BaseModel):
    area: Area
    dt: datetime
    actual_result: int
    forecast_demand: int
    forecast_supply: int

    @property
    def forecast_usage_pc(self):
        return int(self.forecast_demand / self.forecast_supply * 100)


class AreaDemandForecast(BaseModel):
    area: Area
    hourly_forecast_list: List[DemandForecast]
    peak_demand: DemandForecast
    peak_usage: DemandForecast
