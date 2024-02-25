import datetime
mytime=datetime.datetime.now()
print("now=",mytime)

print("\n")
print("Current Year :",mytime.year)
print("Current Month :", mytime.month)
print("Current Day :", mytime.day)
print("\n")
print(mytime.strftime("%B"))
print(mytime.strftime("%b"))
print("\n")
print("\n",mytime.year,"\n",mytime.month,"\n",mytime.day,"\n",mytime.hour,"\n",mytime.minute,"\n",mytime.second,"\n",mytime.microsecond)