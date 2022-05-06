from datetime import date, datetime
from zoneinfo import ZoneInfo


def now() -> datetime:
    return datetime.now(timezone())


def today() -> date:
    return now().date()


def timezone() -> ZoneInfo:
    return ZoneInfo("Asia/Tokyo")
