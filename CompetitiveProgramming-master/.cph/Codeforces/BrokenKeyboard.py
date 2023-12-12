# t = int(input())
# for _ in range(t):
#     s = input()

#     faulty = []
#     correct = set()
#     if len(set(s))<3:
#         print(0)
#     else: 
#         for i in range(len(s)-1):
#             if all(s[i] == s[i+1]):
#                 faulty.append(s[i])
#         print (faulty)
#         for letter in s:
#             if letter not in faulty:
#                 correct.add(letter)
                
#     print(correct)
t = int(input())
for _ in range(t):
    s = input()

    faulty = []
    correct = set()

    for i in range(len(s)-1):
        if (s[i] == s[i+1]):
            faulty.append(s[i])
        
    print(faulty)

    correct = set(s) - set(faulty)
                
    print(correct)


