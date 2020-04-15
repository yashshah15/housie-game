import random
def rand_index(ip):
    return(random.randint(0,len(ip)-1))

d={}
c=1
for i in range(1,10):
    d[i]=[]
    for j in range(c,c+10):
        d[i].append(j)
    c=i*10+1
for i in d.items():
    print(i)
n=int(input("Enter the no of tickets"))    
tickets={}
for i in range(1,n+1):
    tickets[i]=[]
    for j in range(3):
        l=[]
        for k in range(9):
            l.append(0)
        tickets[i].append(l)
for i in tickets.items():
    print(i)

temp=[]
for i in range(6):
    temp.append([])
for i in range(6):
    for j in range(1,10):
        num=rand_index(d[j])
        print(d[j])
        print(num)
        temp[i].append(d[j][num])
        d[j].pop(num)
di=[]
di.append([1,2,4,7,8,9])
di.append([2,3,5,6,8,9])
di.append([1,2,3,6,7,9])
di.append([1,3,4,5,6,8])
di.append([2,3,4,5,7,9])
di.append([1,4,5,6,7,8])
l=[0,1,2,3,4,5]
random.shuffle(l)
random.shuffle(di)
print(l)
print(di)
for i in range(6):
    t=rand_index(di)
    tl=rand_index(l)
    for j in di[t]:
        num=rand_index(d[j])
        temp[l[tl]].append(d[j][num])
        d[j].pop(num)
    l.pop(tl)
    di.pop(t)
for i in temp:
    print(i)
    