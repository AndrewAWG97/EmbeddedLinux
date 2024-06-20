#!/bin/python3

import math

r = int(input("Enter Radius of circle to calculate area: "))
Area = (r**3) * (math.pi)

Area = f"{Area:.2f}"
print(f"Area of circle is {Area}")

