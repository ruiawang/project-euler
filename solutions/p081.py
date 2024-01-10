"""
We can use dynamic programming to find the minimal path sum. At each entry in the matrix - the min path sum for that entry is the entry's value plus the smaller between the min path sum of the child entry on the right of our entry and the maximum path sum of the child entry beneath our entry, accounting for edge cases. We compute bottom-up, starting at the bottom-right of the matrix and iterating upwards towards the top-left.
"""
def solve():
    matrix = []
    with open('0081_matrix.txt', 'r') as f:
        for line in f:
            matrix.append([int(x) for x in line.split(',')])
    M = len(matrix)
    N = len(matrix[0])
    for i in reversed(range(M)):
        for j in reversed(range(N)):
            if i == M - 1 and j == N - 1:
                continue
            elif i == M - 1:
                matrix[i][j] += matrix[i][j+1]
            elif j == N - 1:
                matrix[i][j] += matrix[i+1][j]
            else:
                matrix[i][j] += min(matrix[i][j+1], matrix[i+1][j])
    return matrix[0][0]

if __name__ == "__main__":
    print(solve())