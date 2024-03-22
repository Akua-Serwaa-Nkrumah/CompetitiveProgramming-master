from collections import defaultdict

class UnionFind:
    def __init__(self,account):
        self.par = {}
        self.size = {}

        for acc in account:
            for i in range(1,len(acc)):
                self.par[acc[i]] = acc[i] 
                 
                if acc[i] not in self.size:
                    self.size[acc[i]] = 1
                else:
                    self.size[acc[i]] += 1

    def find(self,i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])

        return self.par[i]

    def union(self,x,y):
        x_par = self.find(x)
        y_par = self.find(y)

        if x_par == y_par:
            return

        if self.size[x_par] < self.size[y_par]:
            self.par[x_par] = y_par
            self.size[y_par] += self.size[x_par]

        else:
            self.par[y_par] = x_par
            self.size[x_par] += self.size[y_par]


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        accountFind = UnionFind(accounts)

        people = {}

        for acc in accounts:
            for i in range(1,len(acc)):
                people[acc[i]] = acc[0]

        for acc in accounts:
            for i in range(2,len(acc)):
                accountFind.union(acc[i-1],acc[i])

        res = defaultdict(list)
        cur = []

        for parent in accountFind.par:
            cur.append((parent,accountFind.find(parent)))
            res[accountFind.find(parent)].append(parent)

        ans = []
        for r in res:
            cur = [people[r]]
            res[r].sort()
            cur.extend(res[r])
            ans.append(cur)

        return ans