import math
import random
# # Q2
# print('AZ vaccination reservation at UTAR')
# Input_year = int(input('Enter Year          (4 Digits) >> '))
# Input_month = int(input('Enter Month         (2 Digits) >> '))
# print()
# print('Year:', Input_year, '    ', 'Month:', Input_month)
# print('----------------------------------')
# print('SUN MON TUE WED THU FRI SAT')
# print('----------------------------------')
# Position_List = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# A = 0
# day = Input_year - 1 % 400
# day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
# day = day % 7
# space = ''
# if Input_year % 4 == 0:
#     for i in range(Input_month - 1):
#         A += leap_year[i]
# else:
#     for i in range(Input_month - 1):
#         A += non_leap_year[i]
# day += A % 7
#
# if Input_month == 9 or Input_month == 4 or Input_month == 6 or Input_month == 11:
#     for i in range(31 + day):
#         if i <= day:
#             print(space, end='  ')
#         else:
#             print("%.2d" % (0), end='  ')
#             if (i + 1) % 7 == 0:
#                 print()
# elif Input_month == 2:
#     if Input_year % 4 == 0:
#         p = 30
#     else:
#         p = 29
#     for i in range(p + day):
#         if i <= day:
#             print(space, end='  ')
#         else:
#             print("%.2d" % (0), end='  ')
#             if (i + 1) % 7 == 0:
#                 print()
# else:
#     for i in range(32 + day):
#         if i <= day:
#             print(space, end='  ')
#         else:
#             print("%.2d" % (0), end='  ')
#             if (i + 1) % 7 == 0:
#                 print()
#
# print()
# Vaccine_Date = input('Date of Vaccination (DD/MM/YYYY) >> ')
# Position = Position_List.index(Vaccine_Date[3:5])
# if Vaccine_Date[3:5] >= '10':
#     if Vaccine_Date[3:5] != str(Input_month):
#         print('Invalid Month')
#         quit()
#     elif Vaccine_Date[6:10] != str(Input_year):
#         print('Invalid Year')
#         quit()
#     elif str(Vaccine_Date[:2]) > str(non_leap_year[Position]):
#         print('Invalid Date')
# else:
#     if Vaccine_Date[4:5] != str(Input_month):
#         print('Invalid Month')
#         quit()
#     elif Vaccine_Date[6:10] != str(Input_year):
#         print('Invalid Year')
#         quit()
#     elif str(Vaccine_Date[:2]) > str(non_leap_year[Position]):
#         print('Invalid Date')
#         quit()
#
# if Vaccine_Date == 0:
#     quit()
# IC = input('NRIC Number (YYMMDD-SS-NNNN) >> ')
# Current_Year = 21  # 2021
# IC_years = int(str(IC)[:2])
# if 22 <= IC_years <= 99:  # 1922 - 1999
#     Age = 100 - IC_years + Current_Year
# elif IC_years < 22:  # 2000 - 2021
#     Age = Current_Year - IC_years
# if Age < 18:
#     print('Recipient is too young for the vaccination')
# else:
#     print('Done')
#

# Q3
price_list = [150.00, 45.00, 30.00, 20.00, 45.00, 99.90, 89.00, 59.90, 23.00]
item_list = ['Building Blocks', 'Puzzle', 'Doll', 'Shirt', 'Dress', 'Pants', 'Lipstick', 'Lotion', 'Face Mask']
Category = 1
Total_Price = 0
Selected = []
Selected_Units = []
while Category != '0':
    print()
    print('1. Toys')
    print('2. Clothing')
    print('3. Doll')
    Category = input('Select a category (0 to quit) >> ')
    if Category == '1':
        for i in range(3):
            print(i+1, '.', item_list[i], 'RM', price_list[i])
        Select_item = input('Select an item (1-3) >> ')
        if item_list[int(Select_item) - 1] in Selected:
            Yes = input('You have selected this item. Do you want to add or remove item? (Y/N)')
            Add_Remove = input('Add(A) or Remove(R) >> ')
            if Add_Remove == 'A':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Add_Amount = input('Enter number of unit you wish to add/remove >> ')
                Selected_Units[Position] += int(Add_Amount)
            elif Add_Remove == 'R':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Remove_Amount = input('Enter number of unit you wish to add/remove >> ')
                if int(Remove_Amount) > int(Selected_Units[Position]):
                    print('Operation Fail: The number of items removed is more than the number of selected items')
                else:
                    Selected_Units[Position] -= int(Remove_Amount)
        else:
            Selected.append(item_list[int(Select_item) - 1])
            Units = int(input('Enter number of unit >> '))
            Selected_Units.append(Units)
    elif Category == '2':
        for i in range(3, 6):
            print(i-2, '.', item_list[i], 'RM', price_list[i])
        Select_item = input('Select an item (1-3) >> ')
        if item_list[int(Select_item) - 1] in Selected:
            Yes = input('You have selected this item. Do you want to add or remove item? (Y/N)')
            Add_Remove = input('Add(A) or Remove(R) >> ')
            if Add_Remove == 'A':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Add_Amount = input('Enter number of unit you wish to add/remove >> ')
                Selected_Units[Position] += int(Add_Amount)
            elif Add_Remove == 'R':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Remove_Amount = input('Enter number of unit you wish to add/remove >> ')
                if int(Remove_Amount) > int(Selected_Units[Position]):
                    print('Operation Fail: The number of items removed is more than the number of selected items')
                else:
                    Selected_Units[Position] -= int(Remove_Amount)
        else:
            Selected.append(item_list[int(Select_item) - 1])
            Units = int(input('Enter number of unit >> '))
            Selected_Units.append(Units)
    elif Category == '3':
        for i in range(6, 9):
            print(i-5, '.', item_list[i], 'RM', price_list[i])
        Select_item = input('Select an item (1-3) >> ')
        if item_list[int(Select_item) - 1] in Selected:
            Yes = input('You have selected this item. Do you want to add or remove item? (Y/N)')
            Add_Remove = input('Add(A) or Remove(R) >> ')
            if Add_Remove == 'A':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Add_Amount = input('Enter number of unit you wish to add/remove >> ')
                Selected_Units[Position] += int(Add_Amount)
            elif Add_Remove == 'R':
                Position = Selected.index(item_list[int(Select_item) - 1])
                Remove_Amount = input('Enter number of unit you wish to add/remove >> ')
                if int(Remove_Amount) > int(Selected_Units[Position]):
                    print('Operation Fail: The number of items removed is more than the number of selected items')
                else:
                    Selected_Units[Position] -= int(Remove_Amount)
        else:
            Selected.append(item_list[int(Select_item) - 1])
            Units = int(input('Enter number of unit >> '))
            Selected_Units.append(Units)
print(Selected_Units)
print(Selected)
print('Item                Price(per unit)            Total Unit        Total')
print('----------------------------------------------------------------------')
for k in range(len(Select_item)):
    Position = item_list.index(Selected[k])
    Total_Price += price_list[Position] * Selected_Units[k]
    print(Selected[k], 'RM', price_list[Position], Selected_Units[k], 'RM', price_list[Position] * Selected_Units[k])