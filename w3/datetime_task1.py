import datetime 
import dateutil.relativedelta

# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Сегодня 

dt_now = datetime.datetime.now()
print (dt_now) 

tday = datetime.date.today()
print(tday)

# Вчера 

onedaydelta = datetime.timedelta(days=1)
yesterday = tday - onedaydelta
print(yesterday)

# Месяц назад версия 1 

monthdelta = datetime.timedelta(days=30)
monthago = tday - monthdelta
print(monthago)

# Месяц назад версия 2, слизанная почти 1 в 1 со стаковерфлоу

monthago2 = dt_now - dateutil.relativedelta.relativedelta(months=1)

# Осталось до Новогодней ночи :)

NYnight = datetime.date(2018, 12, 31)
till_NY = NYnight - tday
print(till_NY) 
