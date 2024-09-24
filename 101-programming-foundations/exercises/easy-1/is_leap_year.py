'''
Checks any year greater than 0,
returns True if the year is a leap year, or False if it is not.
'''
# To determine whether a given year is a leap year, 
# use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

def is_leap_year(user_year):
    check400 = user_year % 400
    check100 = user_year % 100
    check4 = user_year % 4

    if user_year < 1752 and user_year % 4 == 0:
        return True
    elif check100 == 0:
        return False if (check400 != 0) else True
    elif check4 == 0:
        return True if (check100 != 0) else False
    elif check400 == 0:
        return True
    else:
        return False

# simpler solution
# def is_leap_year(year):
#     if year < 1752 and year % 4 == 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)