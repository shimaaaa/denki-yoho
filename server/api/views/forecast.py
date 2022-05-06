from typing import List

from data.forecast import AreaDemandForecast
from pydantic import BaseModel
from services import DemandForecastService


class ForecastListResponse(BaseModel):
    data: List[AreaDemandForecast]


def forecast_list() -> ForecastListResponse:
    service = DemandForecastService()
    forecast_list = service.list()
    return ForecastListResponse(data=forecast_list)
