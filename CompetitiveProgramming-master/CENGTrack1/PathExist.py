from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: [[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_list = defaultdict(set)

        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        if destination in adj_list[source]:
            return True

        visited =set()

        def search(source,destination,visited):
            if source == destination:
                return True

            if destination in adj_list[source]:
                return True

            for node in adj_list[source]:
                if node not in visited:
                    visited.add(node)

                    found = search(node,destination,visited)
                    if found: return True

        return search(source,destination,visited)



            
        