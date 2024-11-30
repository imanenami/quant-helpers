from ..models import MarketDataPoint


def holiday_check(dp: MarketDataPoint) -> bool:
    """Checks whether holiday conditions are met at the provided data point

    Args:
        dp (MarketDataPoint): input data point to check the holiday condition

    Returns:
        bool: True if holiday
    """
    if dp.time.isoweekday() in (6, 7):
        return True
    if dp.time.isoweekday() == 1 and dp.time.hour < 4:
        return True
    if dp.time.isoweekday() == 5 and dp.time.hour > 20:
        return True

    return False
