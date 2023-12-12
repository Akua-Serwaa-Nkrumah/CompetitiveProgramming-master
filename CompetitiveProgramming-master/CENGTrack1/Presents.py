n = int(input())
gifts = list(map(int,input().split()))
present = [0]*n
for gift in gifts:
   present[gift-1] = gifts.index(gift)+1
    
print(*present)
