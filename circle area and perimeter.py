#importing value of pi
from math import pi
print(pi)

#defining function
def circle_info(r, isArea):
    if isArea == True:
        Area = pi*r*r
        return round(Area, 2)
    else:
        perimeter = 2*pi*r
        return round(perimeter, 2)
