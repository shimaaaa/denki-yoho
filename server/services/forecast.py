from datetime import date, timedelta
from itertools import groupby
from typing import List, Optional

from data.forecast import AreaDemandForecast, DemandForecast
from helpers.datetime import today
from repositories.forecast import DemandForecastRepositories


def _area_grouper(x):
    return x.area


class DemandForecastService:
    def list(self) -> AreaDemandForecast:
        target_date = today()
        repos = DemandForecastRepositories()
        forecasts = repos.list(target_date=target_date)
        if not forecasts:
            # use latest date data
            target_date = repos.get_latest_date()
            assert target_date is not None
            forecasts = repos.list(target_date=target_date)
        forecasts.sort(key=_area_grouper)

        results = []
        for area, group in groupby(forecasts, key=_area_grouper):
            peak_demand: Optional[DemandForecast] = None
            peak_usage: Optional[DemandForecast] = None
            forecast_list = list(group)
            for data in forecast_list:
                if not peak_demand or data.forecast_demand > peak_demand.forecast_demand:
                    peak_demand = data
                if not peak_usage or data.forecast_usage_pc > peak_usage.forecast_usage_pc:
                    peak_usage = data
            results.append(
                AreaDemandForecast(
                    area=area, hourly_forecast_list=forecast_list, peak_demand=peak_demand, peak_usage=peak_usage
                )
            )
        return results

    def bulk_save(self, records: List[DemandForecast]):
        repos = DemandForecastRepositories()
        return repos.bulk_save(records)
