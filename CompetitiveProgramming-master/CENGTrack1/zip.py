
N,X = map(int,input().split())

subject = []
for i in range(X):
    marks = list((map(float,input().split())))
    subject.append(marks)
   
subject = list(zip(*subject))
for mark in subject:
    print(sum(mark)/len(mark))

