import math
import random
# Q2
print('AZ vaccination reservation at UTAR')
Input_year = input('Enter Year          (4 Digits) >> ')
Input_month = input('Enter Month         (2 Digits) >> ')
print()
print('Year:', Input_year, '    ', 'Month:', Input_month)
print('--------------------------------------------------')
print('SUN    MON    TUE    WED    THU    FRI    SAT')
print('--------------------------------------------------')
non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
A = 0
if Input_year % 4 == 0:
    for i in range(mm - 1):
        A += leap_year[i]
else:
    for i in range(mm - 1):
        A += non_leap_year[i]
day += A % 7
day = day % 7





Current_Year = 21  # 2021
IC_years = int(str(IC)[:2])
if 22 <= IC_years <= 99:  # 1922 - 1999
    Age = 100 - IC_years + Current_Year
elif IC_years < 22:  # 2000 - 2021
    Age = Current_Year - IC_years
print(Age)
# Q3