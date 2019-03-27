#program to sort the items in list without using a function
'''With List:
append
extend
remove
copy
sort
insert
delete
pop
clear
index
count
reverse'''







'''q23
st=int(input("enter the number of values you want to insert in machine "))
li=[]
for a in range(0,st):
    k=int(input("\n"))
    li.append(k)
print(li)
for b in li:
    if(b%2==0):
        print(b,"is even")
    else:
        print(b,"is odd")'''
    


'''q24
st=int(input("enter the number of values you want to insert in machine "))
li=[]
for a in range(0,st):
    k=int(input("\n"))
    li.append(k)
print(li)
for b in li:
    for c in li:
        if (b<c):
            li.remove(b)
        else :
            continue
print(b)'''

'''q22
st=int(input("enter the number of values you want to insert in machine "))
li=[]
for a in range(0,st):
    k=int(input("\n"))
    li.append(k)
print(li)
for b in li:
    for c in li:
        if (b>c):
            li.remove(c)
        else :
            continue
print(c)
'''

'''Q21.
st=int(input("enter the number of values you want to insert in machine "))
li=[]
for a in range(0,st):
    k=int(input("\n"))
    li.append(k)
print(li)
new=[]
for b in li[0:st]:
    maxi=max(li)
    new.append(maxi)
    li.remove(maxi)
print(new)'''


