from collections import defaultdict
# Function to convert Edge List to Adjacency List
def edge_list_to_adjacency_list(edge_list):
    adj_list = defaultdict(list)
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])

    return adj_list

print(edge_list_to_adjacency_list([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]))
