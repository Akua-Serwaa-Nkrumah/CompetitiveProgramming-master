# Function to convert Adjacency List to Adjacency Matrix
def adjacency_list_to_matrix(adj_list):
    n  = len(adj_list)
    adj_matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for num in adj_list[i]:
            adj_matrix[i][num] = 1

    return adj_matrix

print(adjacency_list_to_matrix([[1,2],[2],[0,3],[3]]))
