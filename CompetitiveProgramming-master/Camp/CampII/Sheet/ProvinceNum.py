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

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        connect = UnionFind(len(isConnected))
        numComp = len(isConnected)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and connect.find(i+1) != connect.find(j+1):
                    connect.union(i+1,j+1)
                    numComp -= 1

        return numComp