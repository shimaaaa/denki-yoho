import csv
from datetime import datetime
from io import StringIO
from typing import List

from commands.importer.base import DataDownloader, DataTransformer, Importer
from data.forecast import DemandForecast
from helpers.constants import Area


class TokyoDataDownloader(DataDownloader):
    URL = "https://www.tepco.co.jp/forecast/html/images/juyo-s1-j.csv"

    def run(self) -> str:
        return self._fetch(url=self.URL)


class TokyoDataTransformer(DataTransformer):
    FORECAST_HEADER = "DATE,TIME,当日実績(万kW),需要電力予測値(万kW),供給力予測値(万kW),使用率(%)"

    @classmethod
    def _extract(cls, raw_data: str) -> str:
        start_idx = raw_data.find(cls.FORECAST_HEADER)
        raw_data = raw_data[start_idx:]
        end_idx = raw_data.find("\r\n\r\n")
        return raw_data[:end_idx]

    @classmethod
    def _structuralize(cls, raw_data: str) -> List[DemandForecast]:
        structured_data = []
        reader = csv.DictReader(StringIO(raw_data), delimiter=",")
        for row in reader:
            dt = datetime.strptime(f"{row['DATE']} {row['TIME']}", "%Y/%m/%d %H:%M")
            structured_data.append(
                DemandForecast(
                    area=Area.tokyo,
                    dt=dt,
                    actual_result=row["当日実績(万kW)"],
                    forecast_demand=row["需要電力予測値(万kW)"],
                    forecast_supply=row["供給力予測値(万kW)"],
                )
            )
        return structured_data

    def run(self, raw_data: str):
        extracted_data = self._extract(raw_data)
        structured_data = self._structuralize(extracted_data)
        return structured_data


def import_tokyo_forecast():
    importer = Importer(download_strategy=TokyoDataDownloader(), transformer_strategy=TokyoDataTransformer())
    importer.run()
