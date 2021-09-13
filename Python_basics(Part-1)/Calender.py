import calendar
from datetime import date
#Month of the Calender
y = int(input("Year: "))
m = int(input("Month: "))
print(calendar.month(y,m))

#Calculate number of days between two dates
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = f_date - l_date
print(delta)


