import math
x1, y1 = 39.9075000, 116.3952300
x2, y2 = 50.4546600, 30.5233000
x1, y1 = math.radians(x1), math.radians(y1)
x2, y2 = math.radians(x2), math.radians(y2)
R = 6371.032
distance = R * math.acos(math.sin(x1) * math.sin(x2) +
                         math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print(f"Distance: {distance:>10.3f} km")
