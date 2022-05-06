from datetime import date
from typing import List, Optional

from data.forecast import DemandForecast
from helpers.constants import Area
from models import Engine
from models.forecast import DemandForecast as DemandForecastModel
from sqlalchemy import Date, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session


class DemandForecastRepositories:
    def _from_model(self, model: DemandForecastModel) -> DemandForecast:
        return DemandForecast(
            area=model.area,
            dt=model.dt,
            actual_result=model.actual_result,
            forecast_demand=model.forecast_demand,
            forecast_supply=model.forecast_supply,
        )

    def list(self, target_date: Optional[date] = None, area: Optional[Area] = None):
        session = Session(Engine)
        stmt = select(DemandForecastModel)
        if target_date:
            stmt = stmt.where(DemandForecastModel.dt.cast(Date) == target_date)
        if area:
            stmt = stmt.where(DemandForecastModel.area == area)
        results = []
        for row in session.scalars(stmt):
            results.append(self._from_model(model=row))
        return results

    def bulk_save(self, records: List[DemandForecast]):
        stmt = postgresql.insert(DemandForecastModel)
        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=["area", "dt"],
            set_={
                "actual_result": stmt.excluded.actual_result,
                "forecast_demand": stmt.excluded.forecast_demand,
                "forecast_supply": stmt.excluded.forecast_supply,
            },
        )
        session = Session(Engine)
        session.execute(statement=upsert_stmt, params=[record.dict() for record in records])
        session.commit()
