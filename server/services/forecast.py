from typing import List

from data.forecast import DemandForecast
from models import Engine
from models.forecast import DemandForecast as DemandForecastModel
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session


class DemandForecastService:
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
        session.execute(
            statement=upsert_stmt, params=[record.dict() for record in records]
        )
        session.commit()

    # area = Column(
    #     Enum(Area, name="demand_forecast_area", create_type=False), nullable=False
    # )
    # dt = Column(DateTime, nullable=False)
    # actual_result = Column(Integer, nullable=False)
    # forecast_demand: Column(Integer, nullable=False)
    # forecast_supply: Column(Integer, nullable=False)
