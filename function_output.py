#!/usr/bin/env python3

# def formatname(fname, lname):
#     if fname == "" or lname == "":
#         return "You didn't provide valid inputs."
#     formatted_fname = fname.title()
#     formatted_lname = lname.title()
#     return f"Result: {formatted_fname} {formatted_lname}"

# print(formatname(input("What is your first name?"), input("What is your last name?")))

#Interactive Days in Month

def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    if month > 12 or month < 1:
        return "Invalid month"
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year) and month == 2:
        return 29
    return monthdays[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(days)
