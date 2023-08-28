#!/usr/bin/env python3


studentscores = {"eli": 81, "shreya": 90, "parmis": 95, "mahnaz": 78, "rutvi": 86 }

studentgrades = {}

for student in studentscores:
    score = studentscores[student]
    if score > 90:
        studentgrades[student] = "Outstanding"
    elif score > 80:
        studentgrades[student] = "Exceeds Expectations"
    elif score > 70:
        studentgrades[student] = "Acceptable"
    else:
        studentgrades[student] = "Fail"
        
print(studentgrades)

#Nesting Dictionary in Dictionary
# travellog = {"Europe": {"cities visited": ["Milan", "Florence", "Siena", "Rome", "Oxford", "Paris"], "total visits": 6},
# "World": {"countries visited": ["US", "Canada", "France", "UK", "Italy"], "total visits": 5}}

# #Nesting Dictionary in List

# def addnewcountry(country_visited, times_visited, cities_visited):
#     newcountry = {}
#     newcountry["country"] = country_visited
#     newcountry["visits"] = times_visited
#     newcountry["cities"] = cities_visited
#     travellog.append(newcountry)

# addnewcountry("Mexico", 3, ["South Korea", "Greece", "Australia"])
# print(travellog)

