
t = int(input())
for _ in range(t):
    s, x = input().split()
    x = int(x)
    count = 0
    HH, MM = int(s[:2]), int(s[3:])
    
    h_t = x//60
    m_t = x%60
        
    hr = h_t + HH
    min = m_t + MM
    
    while s != str(hr-24) + ":" + str(min-60):
        hr += h_t
        min += m_t
        
        if min > 59:
            hr += 1
            min = min%60
            
        if str(hr) + ":" + str(min) == reversed(str(hr) + ":" + str(min)):
            count += 1
            
    print(count)
 