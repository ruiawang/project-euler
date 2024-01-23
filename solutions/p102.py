"""
We can use the sign of the cross products to check if the origin is in the triangle
Explanation:
For points A,B,C that form a triangle, and point P, if we examine the cross products:
AB x AP, BC x BP, CA x CP
for 2D triangles these cross products will be a 3d vector with only non-zero entry in the 3rd slot. If we examine the sign of the third slot, P is inside the triangle ABC if and only if the sign on the third slot across A,B,C is equal.
Since our point of interest, P is the origin, AP, BP, CP are just the respective vectors A,B,C.
"""
def sign(x):
    """sign function"""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else: 
        return 0

def contains_origin(x_1, y_1, x_2, y_2, x_3, y_3):
    """Uses sign of cross products to check if origin in the triangle"""
    A = sign((x_2 - x_1)*y_1 - (y_2 - y_1)*x_1)
    B = sign((x_3 - x_2)*y_2 - (y_3 - y_2)*x_2)
    C = sign((x_1 - x_3)*y_3 - (y_1 - y_3)*x_3)
    return A==B==C

def solve():
    coordinates = []
    with open('0102_triangles.txt', 'r') as f:
        for line in f:
            coordinates.append([int(x) for x in line.split(',')])
    return sum(1 for coords in coordinates if contains_origin(*coords))

if __name__ == "__main__":
    print(solve())
