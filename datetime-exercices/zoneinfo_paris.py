from datetime import datetime
from zoneinfo import ZoneInfo

paris = ZoneInfo('Europe/Paris')
utc = ZoneInfo('UTC')

now_local = datetime.now(paris)
now_utc = now_local.astimezone(utc)

print(now_local.strftime('%Y-%m-%d %H:%M:%S %Z'))