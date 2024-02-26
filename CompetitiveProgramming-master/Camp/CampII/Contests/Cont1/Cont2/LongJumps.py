import sys, threading

def main():
    def dp(i):
        if i >= n:
            return 0
        
        if i not in memo:
            memo[i] = a[i] + dp(i+a[i])

        return memo[i]
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        memo= {}
        mx = 0

        for i in range(n):
            mx = max(mx,dp(i))

        print(mx)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
