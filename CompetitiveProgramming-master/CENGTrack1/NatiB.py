group = []
print('How many students are in the group?')
student_num = int(input())
for i in range(student_num):
    members = input()
    group.append(members)

for j in group:
    for i in range(len(j)):
        if(j[i] == '#'):
            j[i].replace('#',' ')
    print(j)