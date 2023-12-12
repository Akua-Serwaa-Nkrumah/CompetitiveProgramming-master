n, d = map(int,input().split())

amount_to_factor = {}
for _ in range(n):
    amount, factor = map(int,input().split())
    amount_to_factor[amount] = factor
    
print(amount_to_factor)
