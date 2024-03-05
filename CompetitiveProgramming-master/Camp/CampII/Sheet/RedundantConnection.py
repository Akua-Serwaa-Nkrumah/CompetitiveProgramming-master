class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.size = {}

        for i in range(1,n+1):
            self.par[i] = i
            self.size[i] = 1

    def find(self,i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        
        return self.par[i]

    def union(self,u,v):
        u_find = self.find(u)
        v_find = self.find(v)

        if u_find != v_find:
            if self.size[u_find] <= self.size[v_find]:
                self.par[u_find] = v_find
                self.size[v_find] += self.size[u_find]

            else:
                self.par[v_find] = u_find
                self.size[u_find] += self.size[v_find]

            return

        return [u,v]

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        edgeUnion = UnionFind(len(edges))

        for j in edges:
            if edgeUnion.union(j[0],j[1]):
                return edgeUnion.union(j[0],j[1])
