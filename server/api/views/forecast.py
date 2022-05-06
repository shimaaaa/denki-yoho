from typing import List

from data.forecast import AreaDemandForecast
from helpers.datetime import today
from pydantic import BaseModel
from services import DemandForecastService


class ForecastListResponse(BaseModel):
    data: List[AreaDemandForecast]


def forecast_list() -> ForecastListResponse:
    service = DemandForecastService()
    target_date = today()
    forecast_list = service.list(target_date=target_date)
    return ForecastListResponse(data=forecast_list)
