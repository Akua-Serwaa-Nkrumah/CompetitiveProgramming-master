def solve(s):
    s_date = s.split()
    print(s_date)
    diction = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05'}

    ans = [""]*3
    ans[0] += s_date[2]
    ans[1] += diction[s_date[1]]
    if len(s_date[0]) == 3:
        ans[2] = '0' 

    else:
        ans[2] = ''

    ans[2] += s_date[0][:-2]
    
    return '-'.join(ans)
print(solve('1st Mar 1974'))

