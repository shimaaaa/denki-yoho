from abc import ABC, abstractmethod
from typing import List

import requests
from data.forecast import DemandForecast
from services import DemandForecastService


class DataDownloader(ABC):
    def _fetch(self, url: str):
        header = {"User-Agent": ""}
        response = requests.get(url, headers=header)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text

    @abstractmethod
    def run() -> str:
        pass


class DataTransformer(ABC):
    @abstractmethod
    def run(cls, raw_data: str) -> List[DemandForecast]:
        pass


class Importer:
    def __init__(
        self,
        download_strategy: DataDownloader,
        transformer_strategy: DataTransformer,
    ) -> None:
        self._download_strategy = download_strategy
        self._transformer_strategy = transformer_strategy

    def _save(self, structured_data: List[DemandForecast]):
        service = DemandForecastService()
        service.bulk_save(records=structured_data)

    def run(self):
        raw_data = self._download_strategy.run()
        transformed_data = self._transformer_strategy.run(raw_data=raw_data)
        self._save(structured_data=transformed_data)
