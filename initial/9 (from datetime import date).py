import datetime
from datetime import date

now=date.today()
print(now)
print("\n")
print(datetime.date(2003, 12 , 2))
print(now.strftime("%m-%d-%y."" %d %b %Y is a %A on" " %d day of %B"))
#change
print(now.strftime("%m-%d-%y."" %d %b %Y is a %a on" " %d day of %B"))
print("\n")
#date support arithmatic calender
now=date.today()
birthday=date(2002, 1, 14)
age=now-birthday
print(age.days)
