"""
This problem can be reduced to finding the minimum spanning tree (MST) of a weighted graph.
We can find the total cost of such MST through Prim's algorithm.
We can find the savings by comparing it to the original weight of the graph, which is given by
one-half of the sum of all finite weights in the matrix (since it is symmetric)
"""
import csv
import heapq

def solve():
    # reading in the file
    matrix = [[0 for _ in range(40)] for _ in range(40)]
    with open('0107_network.txt', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            for j, val in enumerate(row):
                if val == '-':
                    matrix[i][j] = float('inf')
                else:
                    matrix[i][j] = int(val)
    TOTAL_COST = sum(matrix[i][j] for i in range(40) for j in range(40) if matrix[i][j] != float('inf')) // 2
    
    # Prim's Algorithm
    mst_cost = 0
    visited = set()
    heap = [(val, i) for i, val in enumerate(matrix[0])]
    heapq.heapify(heap)
    visited.add(0)
    while heap:
        cost, dest = heapq.heappop(heap)
        if dest in visited or cost == float('inf'):
            continue
        visited.add(dest)
        mst_cost += cost
        for i, val in enumerate(matrix[dest]):
            if i not in visited and val != float('inf'):
                heapq.heappush(heap, (val, i))

    return TOTAL_COST - mst_cost

if __name__ == "__main__":
    print(solve())
        