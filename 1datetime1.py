
# from datetime import datetime
# #import datetime year = datetime.date.today().year.


# current_datetime = datetime.now()

# sh_da = dir(current_datetime)
# c_d = current_datetime

# print()
# print(c_d)
# print()
# print(sh_da)
# print()


#Task1

#dt_year = datetime.date.today().year
# dt_year2 = c_d.today().year
# look_year = datetime.today().year

# print()
# print(c_d)
# print()
# print(look_year)
# print()
# print(dt_year2)
# print()


#Task2

# #dt_year = datetime.date.today().year
# dt_year2 = c_d.today().year
# s_d = datetime(2021, 7, 14)
# look_day = datetime.today().day
# look_day2 = s_d.day
# #today = datetime(2017, 10, 20)
# #toll = today.get_weekday()  # what I look for
# wd = datetime.today().weekday()
# wd2 = s_d.weekday()

# print()
# print(c_d)
# print()
# print(look_day)
# print()
# print(look_day2)
# print()
# print(wd)
# print()
# print(wd2)
# print()


#Task3

# import calendar

# yr = input("Give me a Year: ")
# year = int(yr)
# year1 = yr


# #print(calendar.isleap(year))
# result = calendar.isleap(year)
# if result == True:
#     print(year1 + " is a leap Year!")
# if result == False:
#     print(year1 + " is not a leap Year!")




# def leapyr(n):
#     if n % 400 == 0:
#         return True
#     if n % 100 == 0:
#         return False
#     if n % 4 == 0:
#         return True
#     return False
# print (leapyr(1900))


#Task4


# from datetime import datetime

# date_as_string = "Feb 14 2021 8:30AM"

# result = datetime.strptime(date_as_string, '%b %d %Y %I:%M%p')

# #result1 = datetime.strptime(c_d, '%b %d %Y %I:%M%p')

# #print(result1)

# print()
# print(result)


# date_string = "2012-12-12 10:10:10"
# print (datetime.fromisoformat(date_as_string))
#2012-12-12 10:10:10


# - Your result should look like this:

# ```
# 2021-02-14 08:30:00
# ```


#Task2.1
# import time
# from datetime import datetime, timedelta, date
# import os

# os.system("clear")
# current_datetime = datetime.now()

# tdelta = timedelta(days= 15)
# bday = current_datetime 
# bs_day = datetime.strftime(bday,'%Y-%m-%d')
# print()
# time.sleep(2)
# print("Task2.1")
# print()
# print(bs_day)
# print()
# print("Substract 15 Days:")
# print()
# gday = current_datetime - tdelta
# re_day =datetime.strftime(gday,'%Y-%m-%d')

# print(re_day)


# Using the variable called `current_datetime`, 
# subtract 15 days from the current time.

# from datetime import datetime
# current_datetime = datetime.now()

# d = datetime.strptime("2020-01-22", '%Y-%m-%d')
# print(d)
# print()
# x = d - datetime.timedelta(days=57) # 2019-11-26 00:00:00
# print(x)
# # .strtime()

# from datetime import datetime, timedelta

# current_datetime = datetime.now()

# d = datetime.today()
# new_d = d - timedelta(days=57)

# print(d)
# print(new_d)

# from datetime import datetime
# from datetime import timedelta

# current_datetime = datetime.now()
# c_d = current_datetime
# print(c_d)
# dte_ft = '%d/%m/%Y'
# c_d_Obj = datetime.strptime(c_d, dte_ft)
# print(c_d_Obj)
# given_date = '21/1/2021'
# print('Given Date: ', c_d)
# # Create datetime object from date string
# date_format = '%d/%m/%Y'
# dtObj = datetime.strptime(c_d, date_format)
# # Subtract 10 days from a given datetime object
# n = 10
# past_date = dtObj - timedelta(days=n)
# print('Past Date: ', past_date)
# print('Past Date: ', past_date.date())
# past_date_str = past_date.strftime(date_format)
# print('Past Date as string object: ', past_date_str)

#Task2

#from datetime import datetime, timedelta, date



# current_datetime = datetime.now()
# c_d = current_datetime
# print(c_d)


# date_str = datetime.strftime(current_datetime, '%m/%d/%Y')

# print(date_tim_str)

# a_date = datetime.date(2015, 10, 10)
# days = datetime.timedelta(5)
# new_date = a_date - days #. Subtract 5 days from a_date.
# print(new_date)

#Task 2.2

#from datetime import datetime, timedelta, date, 
#os.system("clear")
# current_datetime = datetime.now()

# tdelta = timedelta(days= 7)
# bday = current_datetime 
# bs_day = datetime.strftime(bday,'%Y-%m-%d')
# print()
# print()
# print()
# time.sleep(2)
# print("Task2.2")
# print()
# print(bs_day)
# print()
# print("Add 7 Days:")
# print()
# gday = current_datetime + tdelta
# re_day =datetime.strftime(gday,'%Y-%m-%d')

# print(re_day)

##Task2.3

from datetime import datetime, timedelta, date

remind_me = "Hello Friedrich, your rent of 300 € is due on 25 January, 2021."

start_date = datetime(year=2022, month=9, day=15)

print() 
for i in range(1,13):
    da_date = date(year=2022, month=i, day=25)
    print("test"+ da_date.strftime({%A the %dth of %B, %Y}))