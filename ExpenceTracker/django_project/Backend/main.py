# Typing
from typing import List, Any, Dict

# Django imports
from django.utils import timezone

# Other imports
from datetime import datetime
from calendar import monthrange


def get_last_7_date(today: datetime = datetime.now()) -> datetime:
    """
    :param today: Today\n
    ______________________\n
    Retuns last 7 days date 
    """

    day: int = today.day
    month: int = today.month
    year: int = today.year

    if day - 7 >= 1:
        last_7_days_date: datetime = datetime(year, month, day - 7)
    else:
        month -= 1
        last_day_of_month: datetime = today.replace(day=monthrange(today.year, month)[1]).day
        day_left: int = abs(7 - day)
        last_7_days_date: datetime = datetime(year, month, last_day_of_month - day_left)
    

    return last_7_days_date

def get_last_30_date(today: datetime = datetime.now()) -> datetime:
    """
    :param today: Today\n
    ______________________\n
    Retuns last 30 days date 
    """

    day: int = today.day
    month: int = today.month
    year: int = today.year

    if day - 30 >= 1:
        last_30_days_date: datetime = datetime(year, month, day - 30)
    else:
        month -= 1
        last_day_of_month: datetime = today.replace(day=monthrange(today.year, month)[1]).day
        day_left: int = 30 - day
        last_30_days_date: datetime = datetime(year, month, last_day_of_month - day_left)
    

    return last_30_days_date

def get_last_365_date(today: datetime = datetime.now()) -> datetime:
    """
    :param today: Today\n
    ______________________\n
    Retuns last 365 days date 
    """

    day: int = today.day
    month: int = today.month
    year: int = today.year

    try:
        return datetime(year - 1, month, day)
    except:
        return datetime(year - 1, month, day - 1)

def get_percentage(total: float, part: float) -> float:
    """
    :param total: The total income or outcome\n
    :param part: The part of income or outcome\n
    _________________________________________________\n
    Calculates the persentage of total
    """

    return (part * 100) / total

def get_total(database: List[Dict[str, Any]]) -> int:
    """
    :param database: Databese of income or outcome\n
    _____________________________________________________\n
    Get the total income/outcome and the last 7 days
    """

    total: int = 0
    for data in database:
        total += data.amount
    return total

def get_total_last_7_days(database: List[Dict[str, Any]]) -> int:
    """
    :param database: Databese of income or outcome\n
    _____________________________________________________\n
    Get the total income/outcome of the last 7 days
    """

    total_7_days: int = 0
    last_7_days: datetime = timezone.make_aware(get_last_7_date())

    for data in database:
        if last_7_days < data.date:
            total_7_days += data.amount
    
    return total_7_days

def get_total_last_30_days(database: List[Dict[str, Any]]) -> int:
    """
    :param database: Databese of income or outcome\n
    _____________________________________________________\n
    Get the total income/outcome of the last 30 days
    """

    total_30_days: int = 0
    last_30_days: datetime = timezone.make_aware(get_last_30_date())

    for data in database:
        if last_30_days < data.date:
            total_30_days += data.amount
    
    return total_30_days

def get_total_last_365_days(database: List[Dict[str, Any]]) -> int:
    """
    :param database: Databese of income or outcome\n
    _____________________________________________________\n
    Get the total income/outcome of the last 365 days
    """

    total_365_days: int = 0
    last_365_days: datetime = timezone.make_aware(get_last_365_date())

    for data in database:
        if last_365_days < data.date:
            total_365_days += data.amount
    
    return total_365_days