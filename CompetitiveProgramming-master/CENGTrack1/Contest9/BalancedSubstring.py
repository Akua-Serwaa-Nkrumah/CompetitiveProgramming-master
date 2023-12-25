from collections import Counter

def solve():
    l, r = 0, n-1
    s_count = Counter(s)

    if s_count['a'] == s_count['b']:
        print (*[l+1,r+1])
        return

    while l < r:
        if s_count['a'] > s_count['b']:
            if s[l] == 'a':
                l += 1
                s_count['a'] -= 1
            elif s[r] == 'a':
                r -= 1
                s_count['a'] -= 1
            else:
                l += 1
                s_count['b'] -= 1

        elif s_count['a'] < s_count['b']:
            if s[l] == 'b':
                l += 1
                s_count['b'] -= 1

            elif s[r] == 'b':
                r -= 1
                s_count['b'] -= 1

            else:
                l += 1
                s_count['a'] -= 1

        else:
            print (*[l+1,r+1])
            return
        
    print (*[-1, -1])
    return


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve()

 