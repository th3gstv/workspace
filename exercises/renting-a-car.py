day = int(input("How much days? "))
km = float(input("How much did you drive? "))
pay = 60*day + 0.15*km
print(f"You've to pay ${pay:.2f} for drive {km}km in {day} days")