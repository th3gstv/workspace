from math import sin, cos, tan, radians
angle = float(input("Insert a angle: "))

x = (sin(radians(angle)))
y = (cos(radians(angle)))
z = (tan(radians(angle)))

print('Sine: {:.2f} \nCossine: {:.2f} \nTangent: {:.2f}  '.format(x, y, z))