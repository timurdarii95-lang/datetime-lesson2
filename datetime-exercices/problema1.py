from datetime import datetime
from zoneinfo  import ZoneInfo

data1 = input("Introdu prima data YYYY-MM-DD: ")
data2 = input("Introdu prima data YYYY-MM-DD: ")

data1_formatat = datetime.strptime(data1, '%Y-%m-%d')
data2_formatat = datetime.strptime(data2, '%Y-%m-%d')

dif = data2_formatat - data1_formatat
print(dif)