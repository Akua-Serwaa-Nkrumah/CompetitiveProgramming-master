class UnionFind:
    def __init__(self,string):
        self.par = {}
        self.size = {}

        for s in string:
            self.par[s[0]] = s[0]
            self.size[s[0]] = s[0]

            self.par[s[-1]] = s[-1]
            self.size[s[-1]] = s[-1]

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
        else:
            return u_find == v_find

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        equaFind = UnionFind(equations)

        for equation in equations:
            if equation[1:3] == "==":
                equaFind.union(equation[0],equation[-1])

        check = True
        for equation in equations:
            if check:
                if equation[1:3] == "!=":
                    check = equaFind.find(equation[0]) != equaFind.find(equation[-1])
                else:
                    check = equaFind.find(equation[0]) == equaFind.find(equation[-1])

        return check    