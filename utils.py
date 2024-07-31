import datetime
import pytz
LOCAL_TZ = pytz.timezone('Europe/Warsaw')
SOURCE_TZ = pytz.UTC

def convert_datetime_to_local(utc_datetime: str, format: str):
    datetime_utc = datetime.datetime.strptime(utc_datetime, format)
    datetime_utc = datetime_utc.replace(tzinfo=SOURCE_TZ)
    datetime_local = datetime_utc.astimezone(LOCAL_TZ)
    return datetime_local.strftime(format)

def cut_day_from_date(date_time: str):
    return date_time[:7]