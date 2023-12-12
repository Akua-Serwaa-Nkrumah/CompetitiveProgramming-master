# def countdown(n):
#     print(n)
#     if n == 0:
#         return 0
    
#     countdown(n-1)

# # countdown(7)


# # def countup(number):
# #     n = 0
# #     print(n)
# #     if number == n:
# #         return n
# #     countdown(n + 1)
    
# # countup(2)
# # num = list(range(10))
# # res = {1,2,3}
# # num.append(list(range(3,6)))
# # print(res)
# # print(num)
# # n = 1
# # k = 1
# # state = list(range(1,n+1))
# # cand = [[state[i],state[j]] for i in range(n) for j in range(i+1,n)]
# # print(cand)
# num =[1,2,3,4]
# set1 = {2,1,3}
# # set2 = {[2],[45],[2]}
# # print(set2)
# # num.append(set1.copy())
# # print(set1.issubset(set(num)))
# # print(num)
# # set1 = str(set1)
# # print(set1, type(set1))

# fight = {}
# fight[4,3] = {1,2}
# print(fight[3])

def triangle(n):
    if n == 1:
        return 1
    
    else: 
        return triangle(n-1) + n
    
print(triangle(8))