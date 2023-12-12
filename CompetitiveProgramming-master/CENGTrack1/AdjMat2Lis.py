from collections import defaultdict
# Function to convert Adjacency Matrix to Adjacency List
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = defaultdict(list)
    for i in range(len(adj_matrix)):
        lis = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                lis.append(j)
                
        adj_list[i] = lis

    return adj_list 

print(adjacency_matrix_to_adjacency_list([[0, 1, 1, 0],[0, 0, 1, 0],[1, 0, 0, 1],[0, 0, 0, 1]]))
