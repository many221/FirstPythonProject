# ----------------------------------------

# my_string = "working is working"


# print(len(my_string))
# print(my_string.upper())

# ----------------------------------------

#
# def cube(number):
#     return number ** 3
#
#
# def by_three(number):
#     if number % 3 == 0:
#         return cube(number)
#     else:
#         return False
#
# print(by_three(1))

# ----------------------------------------

# def distance_from_zero(arg):
#     if type(arg) == int or type(arg) == float:
#         return abs(arg)
#     else:
#         return "Nope"
#
#
# print(distance_from_zero(12))
#
# print(distance_from_zero("Hello"))

# ----------------------------------------

def hotel_cost(nights):
    return 140 * nights


# ----------------------------------------
import switcher as switcher


#
# def plane_ride_cost1(city):
#     switcher = {
#         "Charlotte": 183,
#         "Tampa": 220,
#         "Pittsburgh": 222,
#         "Los Angeles": 475,
#     }
#     return switcher.get(city, "Invalid City")


# Didn't except the switch so gotta write as if else statements

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


# print(plane_ride_cost("Charlotte"))


# ----------------------------------------

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif 3 <= days < 7:
        return cost - 20
    else:
        return cost

# print(rental_car_cost(1))

# ----------------------------------------

def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days -1) + plane_ride_cost(city)

print( trip_cost("Charlotte",4))