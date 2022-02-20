from enum import Enum
from typing import List


class Area(str, Enum):
    HOKKAIDO = "hokkaido"
    TOHOKU = "tohoku"
    TOKYO = "tokyo"
    CHUBU = "chubu"
    HOKURIKU = "hokuriku"
    KANSAI = "kansai"
    CHUGOKU = "chugoku"
    SHIKOKU = "shikoku"
    KYUSHU = "kyushu"
    OKINAWA = "okinawa"

    @classmethod
    def areas(cls) -> List[str]:
        return [a.value for a in Area]
