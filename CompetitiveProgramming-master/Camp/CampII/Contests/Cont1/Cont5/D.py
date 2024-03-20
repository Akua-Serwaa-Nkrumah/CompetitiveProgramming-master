class Union:
    def __init__(self,n):
        self.par = {}
        self.cnt = {}

        for i in range(1,n+1):
            self.par[i] = i
            self.cnt[i] = 0

    def find(self, i):
        if self.par[i] == i:
            return i
    
        self.par[i] = self.find(self.par[i])

        return self.par[i]
    
    def union(self,i,j):
        i_find = self.find(i)
        j_find = self.find(j)

        if i_find == j_find:
            self.cnt[i_find] += 1
            if self.cnt[i_find] > 1 and self.cnt[i_find]%2 == 1:
                return True

        else:
            if self.cnt[i_find] > self.cnt[j_find]:
                self.par[j_find] = i_find

            else:
                self.par[i_find] = j_find


t = int(input())

for _ in range(t):
    n = int(input())

    first, sec = set(), set()

    for _ in range(n):
        a,b = map(int,input().split())

        if (a not in first):
            if (b not in first):
                first.add(a)
                first.add(b)

            else:
                if (a not in sec) and (b not in sec):
                    sec.add(a)
                    sec.add(b)

        elif (a not in sec):
            if b not in sec:
                sec.add(a)
                sec.add(b)

    if first == sec and len(first) == n:
        print('YES')

    else:
        print('NO')


