distance = float(input("Choose a distance (meters): "))
km = distance / 1000
hm = distance / 100
dam = distance / 10
m = distance
dm = distance * 10
cm = distance * 100
mm = distance * 1000
print(f'Your distance is {distance} meters\nThis is equivalent to: \n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')