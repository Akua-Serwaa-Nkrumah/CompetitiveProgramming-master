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


# Function to convert Edge List to Adjacency List
def edge_list_to_adjacency_list(edge_list):
    adj_list = defaultdict(list)
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])

    return adj_list


# Function to convert Adjacency List to Adjacency Matrix
def adjacency_list_to_matrix(adj_list):
    n  = len(adj_list)
    adj_matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for num in adj_list[i]:
            adj_matrix[i][num] = 1

    return adj_matrix

print(adjacency_list_to_matrix([[1,2],[2],[0,3],[3]]))

print(edge_list_to_adjacency_list([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]))

print(adjacency_matrix_to_adjacency_list([[0, 1, 1, 0],[0, 0, 1, 0],[1, 0, 0, 1],[0, 0, 0, 1]]))
