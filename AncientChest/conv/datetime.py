from time import mktime
from datetime import datetime, timezone, timedelta


ISO_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DEFAULT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def datetime_to_iso8601(date: datetime) -> str:
    """Datetime convert to string format iso8601.

    Args:
        date (datetime object):

    Returns:
        string: Return iso8601 string format

    Examples:
        >>> print(datetime_to_iso8601(datetime(2020, 8, 7, 14, 13, 13)))
        "2020-08-07T14:30:13+08:00"

    """
    dt = date.replace(tzinfo=timezone(timedelta(hours=8)), microsecond=0).isoformat()
    return dt


def iso8601_to_datetime(date: str) -> datetime:
    """Iso8601 format convert to datetime

    Args:
        date (string):

    Returns:
        datetime object: Return datetime object of input iso8601 string

    Examples:
        >>> print(iso8601_to_datetime("2020-08-07T14:30:13+08:00"))
        datetime.datetime(2020, 8, 7, 14, 13, 13)

    """
    dt = datetime.strptime(date, ISO_DATETIME_FORMAT)
    return dt


def datetime_with_zone_to_unixtime(date: datetime) -> float:
    """Datetime object with time zone convert to unix time

    Args:
        date (datetime object):

    Returns:
        float/int: Return unix time stamp format

    Examples:
        >>> tw_tz = timezone(timedelta(hours=8))
        >>> print(datetime_with_zone_to_unixtime(datetime(2020, 8, 7, 14, 13, 13, tzinfo=tw_tz)))
        1596970680

    """
    dt = mktime(date.timetuple())
    return dt


def unixtime_to_datetime(unix_time: float) -> datetime:
    """Unix time convert to datetime

    Args:
        unix_time (float/int):

    Returns:
        datetime object: Return datetime object of unix time stamp

    Examples:
        >>> print(unixtime_to_datetime(1596970680))
        datetime.datetime(2020, 8, 9, 18, 58, 0)

    """
    dt = datetime.fromtimestamp(unix_time)
    return dt


def datetime_to_unixtime(date: datetime) -> float:
    """Datetime convert to unix time

    Args:
        date (float/int):

    Returns:
        float/int: Return unix time stamp of input date

    Examples:
        >>> print(datetime_to_unixtime(datetime(2020, 8, 9, 18, 58, 0)))
        1596970680

    """
    return mktime(date.timetuple())


def datetime_to_string(date: datetime, pattern: str = DEFAULT_DATETIME_FORMAT) -> str:
    """Datetime convert to string with specific pattern

    Args:
        date (datetime object):
        pattern (string): Set pattern that convert to, example: "%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%H:%M"

    Returns:
        string: Return string format of input datetime object by pattern

    Examples:
        >>> print(datetime_to_string(datetime(2020, 8, 7, 13, 38), "%Y-%m-%d %H:%M:%S"))
        "2020-08-07 13:38:20"

    """
    dt_day = date.strftime(pattern)
    return dt_day


def string_to_datetime(date: str, pattern: str = DEFAULT_DATETIME_FORMAT) -> datetime:
    """Datetime convert to string with specific pattern

    Args:
        date (string):
        pattern (string): Set pattern that convert to, example: "%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%H:%M"

    Returns:
        datetime object: Return datetime object of input string by pattern

    Examples:
        >>> print(string_to_datetime("2020-08-07 13:38:20", "%Y-%m-%d %H:%M:%S"))
        datetime.datetime(2020, 8, 7, 13, 38)

    """

    dt = datetime.strptime(date, pattern)
    return dt
