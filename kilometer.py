# Python program to convert
# Kilometers to miles

def km_to_miles(km):
    miles = km * 0.621371
    return miles
km = float(input("Enter KM: "))
miles = km_to_miles(km)
print(miles,"miles")



