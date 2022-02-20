from data.forecast import DemandPeakForecast, UsagePeakForecast
from helpers.constants import Area
from pydantic import BaseModel
from typing import List


class ForecastListResponse(BaseModel):
    demand: List[DemandPeakForecast]
    usage: List[UsagePeakForecast]


def forecast_list() -> ForecastListResponse:
    return ForecastListResponse(
        demand=[
            DemandPeakForecast(
                area=Area.hokkaido, hour_24=18, max_demand_kw=4054, supply_kw=4868
            )
        ],
        usage=[
            UsagePeakForecast(
                area=Area.hokkaido, hour_24=18, max_demand_kw=4054, supply_kw=4868
            )
        ],
    )
