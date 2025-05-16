from math import hypot
adjacent = float(input("Select an area for adjacent side: "))
opost = float(input("Select an area for opost side: "))
#hypotenuse = pow(pow(adjacent, 2) + pow (opost, 2), 1/2)
    #hypotenuse = (adjacent**2 + opost**2) ** (1/2)
    #print("Your hipotenusa: {:.2f}".format(hypotenuse))
hypotenuse = hypot(adjacent, opost)
print("Hypotenuse: {:.2f}".format(hypotenuse))