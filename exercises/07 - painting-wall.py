#one liter of ink to paint 2m²
print("Put the wall information in meters!")
width = float(input("Width: "))
height = float(input("Height: "))
area = width * height
gallon = area/2
print(f"Your wall dimension is {area} m² and we'll need {gallon}liters of ink to paint your wall")