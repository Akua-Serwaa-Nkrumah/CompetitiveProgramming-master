def Round(m):
    m = str(m)
    m_len = len(m)- 1
    res = 10**m_len
    
    return res


t = int(input())
for _ in range(t):
    m = int(input())
    print(m - Round(m))