# Birthday Day Calculator
# - takes birthday as input
# - prints out years, months, weeks & days since

#Task1

import time
import sys
from datetime import datetime, date, timedelta

def print_slow2(str):
    for letter in str:  #grab each letter
        sys.stdout.write(letter) # pritns out letter
        sys.stdout.flush()  #flush the line and rewrite it
        time.sleep(0.1)


my_b_date1 = input("Enter your Birth Year 'YYYY': ")
my_b_year = my_b_date1
my_b_date2 = input("Enter your Birth Month 'mm': ")
my_b_month = my_b_date2
my_b_date3 = input("Enter your Birth Day 'dd': ")
my_b_day = my_b_date3
my_b_date4 = my_b_year + my_b_month+ my_b_day
#print(my_b_date4)


# a = '20160228'
my_date = datetime.strptime(my_b_date4, '%Y%m%d').strftime('%d/%m/%Y')
# print(my_b_date4)
# print
# print(type(my_b_date4))
print()
print(my_date)
print()
# print(type(my_date))
# print()
b_date_future = "20221117"
my_datex = datetime.strptime(b_date_future, '%Y%m%d').strftime('%d/%m/%Y')
b_fut = datetime.strptime(my_datex, '%d/%m/%Y')

b_date = datetime.strptime(my_date, '%d/%m/%Y')
b_fut_final = ("%d" % ((b_fut - datetime.today()).days))
print()

print("Age in Years : %d" % ((datetime.today() - b_date).days/365))
print()
print("Age in Months : %d" % ((datetime.today() - b_date).days/12))
print()
print("Age in Weeks : %d" % ((datetime.today() - b_date).days/12*4))
print()
print("Age in Days :", ((datetime.today() - b_date).days))
print()

b_date2 = "20211117"
b_date3 = "20211201"
b_date4 = "20221031"
b_date5 = "20221117"
my_date2 = datetime.strptime(b_date2, '%Y%m%d').strftime('%d/%m/%Y')
my_date3 = datetime.strptime(b_date3, '%Y%m%d').strftime('%d/%m/%Y')
my_date4 = datetime.strptime(b_date4, '%Y%m%d').strftime('%d/%m/%Y')
my_date5 = datetime.strptime(b_date5, '%Y%m%d').strftime('%d/%m/%Y')
# print(my_date2)
# print(type(my_date2))
b_datex = datetime.strptime(my_date2, '%d/%m/%Y')
b_datex1 = datetime.strptime(my_date3, '%d/%m/%Y')
b_datex2 = datetime.strptime(my_date4, '%d/%m/%Y')
b_datex3 = datetime.strptime(my_date5, '%d/%m/%Y')
# print(b_datex)
# print(type(b_datex))
#print("Age in Years : %d" % ((b_datex - b_date).days/365))
Years = ("%d" % ((b_datex - b_date).days/365))
#print("Age in Month : %d" % ((b_datex2 - b_datex1).days/365*10))
Month = ("%d" % ((b_datex2 - b_datex1).days/365*10))
#print("Age in Days : %d" % ((b_datex1 - b_datex).days))
Day = ("%d" % ((b_datex1 - b_datex).days))
#print("Age in Days : %d" % ((b_datex3 - b_datex2).days))
Day2 = ("%d" % ((b_datex3 - b_datex2).days))
Days1 = str(Day)
Days2 = str(Day2)
Days3 = int(Days1)
Days4 = int(Days2)

Daysfinal2 = (Days3 + Days4)
Daysfinal = str(Daysfinal2) 
#print(Daysfinal)
#print(type(Daysfinal))
#print(Years)

#print("Age in Years : %d" % ((b_datex - b_date).days/365))

print_slow2("Until my next Birthday on 17.11.2022 ...")
print()
print_slow2("There are " + Years +" Years, "+ Month + " Month, "+ Daysfinal +" Days ... gone!")
time.sleep(1)
print()
print_slow2("... or " + b_fut_final + " Days to go!")
print()

# Event Day Calculator
# - takes date as input
# - prints out years, months, weeks & days until

#from datetime import datetime, date, timedelta

#Task2

# import datetime

# dt  = datetime.datetime
# now = dt.now()


# my_e_date1 = input("Enter your Event Year 'YYYY': ")
# my_e_year = int(my_e_date1)
# my_e_date2 = input("Enter your Event Month 'mm': ")
# my_e_month = int(my_e_date2)
# my_e_date3 = input("Enter your Event Day 'dd': ")
# my_e_day = int(my_e_date3)

# my_e_year1 = my_e_date1
# my_e_month2 = my_e_date2
# my_e_day3 = my_e_date3
# my_e_date4 = str(my_e_day3  + "." + my_e_month2 + "." + my_e_year1) 

# print()
# print("Your Event Date is:" + my_e_date4)

# event2 = dt(my_e_year,my_e_month,my_e_day) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute)

# print()
# print("There are:", event2 , " left to Event Date!")
# print()





# a = '20160228'
# my_date = datetime.strptime(my_e_date4, '%Y%m%d').strftime('%d/%m/%Y')
# print(my_b_date4)
# print
# print(type(my_b_date4))
# print()
# print(my_date)
# print()
# print(type(my_date))
# print()




# This gives timedelta in days
# event1 = dt(year=2022,month=12,day=31) - dt(year=now.year, month=now.month, day=now.day)

# print()
# print(event1)
# print()
# This gives timedelta in days & seconds
#event2 = dt(year=2022,month=12,day=31) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute)



# e_date = datetime.strptime(my_date, '%d/%m/%Y')

# print("Age in Years : %d" % ((datetime.today() + e_date).days/365))
# print()
# #print("Age in Months : %d" % ((datetime.today() + e_date).days*12))
# print()
# print("Age in Weeks : %d" % ((e_date - datetime.today()).days*4))
# print()
# print("Age in Days :", ((e_date - datetime.today()).days))
# print()


# # Personal Project Datetime!
# # - use datetime
# # - surprise us!

#Task3

# import time
# import datetime

# dt  = datetime.datetime
# now = dt.now()


# # my_e_date1 = input("Enter your Event Year 'YYYY': ")
# # my_e_year = int(my_e_date1)
# # my_e_date2 = input("Enter your Event Month 'mm': ")
# # my_e_month = int(my_e_date2)
# # my_e_date3 = input("Enter your Event Day 'dd': ")
# # my_e_day = int(my_e_date3)



# import time
# import sys



# def print_slow(str):
#     for letter in str:  #grab each letter
#         sys.stdout.write(letter) # pritns out letter
#         sys.stdout.flush()  #flush the line and rewrite it
#         time.sleep(0.2)
        
# def print_slow2(str):
#     for letter in str:  #grab each letter
#         sys.stdout.write(letter) # pritns out letter
#         sys.stdout.flush()  #flush the line and rewrite it
#         time.sleep(0.1)

# # print_slow(str)
# # print()
# # time.sleep(1)




# print()
# time.sleep(1)
# print_slow("My personal Event Date? ")
# time.sleep(1)
# print()
# # print()
# # print("My personal Event Date is: ")
# # print()
# my_e_year1 = "2023"
# my_e_month2 = "Juli"
# my_e_day3 = "28"
# my_e_date4 = str(my_e_day3  + "." + my_e_month2 + "." + my_e_year1) 

# print()
# print_slow("My personal Event Date is: " + my_e_date4)
# time.sleep(1)
# print()
# event2 = dt(year=2023,month=7,day=28) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute)

# print()
# print_slow2("Because hopefully after that, ...")
# print()
# print_slow2("I get a Job and therefore ...")
# print()
# print_slow2("my Social Life back, after all !!!")
# print()
# time.sleep(1)
# print()
# print_slow2("Keep Smilling until ...")
# print()
# time.sleep(1)
# print()
# print("Because there are:", event2 , " left to my Event Date!")
# print()