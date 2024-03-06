class UnionFind:
    def __init__(self):
        self.par = {}
        self.size = {}

        for i in 'abcdefghijklmnopqrstuvwxyz':
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
            if [u_find] < [v_find]:
                self.par[v_find] = u_find
                self.size[u_find] += self.size[v_find]

            else:
                self.par[u_find] = v_find
                self.size[v_find] += self.size[u_find]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        stringFind = UnionFind()

        for j in range(len(s1)):
            stringFind.union(s1[j],s2[j])

        ans = ''

        for s in baseStr:
            ans += stringFind.find(s)
                
        return ans
