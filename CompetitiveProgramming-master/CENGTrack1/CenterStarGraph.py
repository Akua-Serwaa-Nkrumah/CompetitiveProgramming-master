from collections import defaultdict
class Solution:
    def findCenter(self, edges: [[int]]) -> int:
        adj_list = defaultdict(set)

        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        for node in adj_list:
            if len(adj_list[node]) == len(edges):
                return node        