t = int(input())
for _ in range(t):
    traffic = list(input().split())
    n, c  = int(traffic[0]), traffic[-1]
    s = input()
    
    c_index = s.index(c)
    g_index = s.index("g")
    
    if c == 'g':
        print(g_index)
        
        
    if c_index < g_index:
        for g in range(g_index+1,int(n)):
            if s[g] == 'g':
                g_index = g
                
        for l in range(c_index+1,g_index):
            if s[l] == c:
                c_index = l
                
        print(g_index - c_index + 1)
    else: 
        print(n,c,'NO')
    # elif c_index > g:
        
        
        
    