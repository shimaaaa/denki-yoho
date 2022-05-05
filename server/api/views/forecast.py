from typing import List

from data.forecast import DemandPeakForecast, UsagePeakForecast
from helpers.constants import Area
from models import Engine, Forecast
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session


class ForecastListResponse(BaseModel):
    demand: List[DemandPeakForecast]
    usage: List[UsagePeakForecast]


def forecast_list() -> ForecastListResponse:
    # session = Session(Engine)
    # stmt = select(Forecast)
    # print(stmt)
    # for user in session.scalars(stmt):
    #     print(user)
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
