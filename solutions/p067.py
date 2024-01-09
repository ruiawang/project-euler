"""
Exactly like p018, we can use dynamic programming to find the maximum path sum. At each number in the triangle - the max path sum for that number is the number's value plus the larger between the maximum path sum of the child number on the left and the maximum path sum of the child number on the right. We compute bottom-up, starting at the bottom of the triangle and finding the 2nd to last layer's max paths, and then iterating upwards.
"""
with open('0067_triangle.txt', mode='r') as f:
    triangle = []
    for line in f:
        triangle.append([int(i) for i in line.split()])

def solve():
    for i in range(len(triangle)- 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

if __name__ == "__main__":
    print(solve())