from collections import Counter
def solve():
    s_count = Counter(s)
    if 'B' in s_count:
        if k == s_count['B']:
            print(k-s_count['B'])
            
        elif k > s_count['B']:
            print(k-s_count['B'])
            print(k-s_count['B'], "B")
            
        else: 
            print(s_count['B'] - k)
            print(s_count['B'] - k, "A")
             
    return

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    solve()
    