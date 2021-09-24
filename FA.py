import math
import random
# Q2
print('AZ vaccination reservation at UTAR')
Input_year = int(input('Enter Year          (4 Digits) >> '))
Input_month = int(input('Enter Month         (2 Digits) >> '))
print()
print('Year:', Input_year, '    ', 'Month:', Input_month)
print('----------------------------------')
print('SUN MON TUE WED THU FRI SAT')
print('----------------------------------')
Position_List = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
A = 0
day = Input_year - 1 % 400
day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
day = day % 7
space = ''
if Input_year % 4 == 0:
    for i in range(Input_month - 1):
        A += leap_year[i]
else:
    for i in range(Input_month - 1):
        A += non_leap_year[i]
day += A % 7

if Input_month == 9 or Input_month == 4 or Input_month == 6 or Input_month == 11:
    for i in range(31 + day):
        if i <= day:
            print(space, end='  ')
        else:
            print("%.2d" % (0), end='  ')
            if (i + 1) % 7 == 0:
                print()
elif Input_month == 2:
    if Input_year % 4 == 0:
        p = 30
    else:
        p = 29
    for i in range(p + day):
        if i <= day:
            print(space, end='  ')
        else:
            print("%.2d" % (0), end='  ')
            if (i + 1) % 7 == 0:
                print()
else:
    for i in range(32 + day):
        if i <= day:
            print(space, end='  ')
        else:
            print("%.2d" % (0), end='  ')
            if (i + 1) % 7 == 0:
                print()

print()
Vaccine_Date = input('Date of Vaccination (DD/MM/YYYY) >> ')
Position = Position_List.index(Vaccine_Date[3:5])
if Vaccine_Date[3:5] >= '10':
    if Vaccine_Date[3:5] != str(Input_month):
        print('Invalid Month')
        quit()
    elif Vaccine_Date[6:10] != str(Input_year):
        print('Invalid Year')
        quit()
    elif str(Vaccine_Date[:2]) > str(non_leap_year[Position]):
        print('Invalid Date')
else:
    if Vaccine_Date[4:5] != str(Input_month):
        print('Invalid Month')
        quit()
    elif Vaccine_Date[6:10] != str(Input_year):
        print('Invalid Year')
        quit()
    elif str(Vaccine_Date[:2]) > str(non_leap_year[Position]):
        print('Invalid Date')
        quit()

if Vaccine_Date == 0:
    quit()
IC = input('NRIC Number (YYMMDD-SS-NNNN) >> ')
Current_Year = 21  # 2021
IC_years = int(str(IC)[:2])
if 22 <= IC_years <= 99:  # 1922 - 1999
    Age = 100 - IC_years + Current_Year
elif IC_years < 22:  # 2000 - 2021
    Age = Current_Year - IC_years
if Age < 18:
    print('Recipient is too young for the vaccination')
else:
    print('Done')

# Q3