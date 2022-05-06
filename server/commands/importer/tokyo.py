import csv
from datetime import datetime
from io import StringIO
from typing import List

import requests
from data.forecast import DemandForecast
from helpers.constants import Area
from services import DemandForecastService


class TokyoDemandForecastImporter:
    URL = "https://www.tepco.co.jp/forecast/html/images/juyo-s1-j.csv"
    FORECAST_HEADER = "DATE,TIME,当日実績(万kW),需要電力予測値(万kW),供給力予測値(万kW),使用率(%)"

    @classmethod
    def _download(cls) -> str:
        header = {"User-Agent": ""}
        response = requests.get(cls.URL, headers=header)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text

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

    @classmethod
    def _save(cls, structured_data: List[DemandForecast]):
        service = DemandForecastService()
        service.bulk_save(records=structured_data)

    @classmethod
    def run(cls):
        raw_data = cls._download()
        extracted_data = cls._extract(raw_data)
        structured_data = cls._structuralize(extracted_data)
        cls._save(structured_data)
