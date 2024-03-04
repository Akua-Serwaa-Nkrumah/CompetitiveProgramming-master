import sys, threading

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a = list(map(int,input().split()))
        a_dict = {}
        a_new = []

        for i in a:
            if i%10 not in a_dict:
                a_dict[i%10] = 1
                a_new.append(i%10)
            else:
                if i%10 == 1 and a_dict[1] < 3:
                    a_dict[1] += 1
                    a_new.append(i%10)

                else:
                    if a_dict[i%10] < 2:
                        a_dict[i%10] += 1
                        a_new.append(i%10)

        memo = {}
        
        def dp(i,pick,cur):
            if pick == 3 and str(cur)[-1] == '3':
                return True
            
            if pick > 3:
                return False

            if i == len(a_new):
                if pick == 3 and str(cur)[-1] == '3':
                    return True
                return False
            if (i,pick,cur) not in memo:
                memo[(i,pick,cur)] = dp(i+1,pick,cur) or dp(i+1,pick+1,cur+a_new[i])

            return memo[(i,pick,cur)]
        
        if dp(0,0,0):
            print('YES')
        else:
            print("NO")

    
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()