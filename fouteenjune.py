'''len()
count()
upper()
lower()
capitalize()
max()
min()
center()
find()
replace()
split()
isalpha()
isspace()
isdigit()
str()
int()
endswith()
startswith()'''
#making else for for and while
#lcm machine
num1=int(input("enter the number 1\n"))
num2=int(input("enter the number 2\n"))
limit=num1*num2
if (num1>num2):
    first=num1
    second=num2
elif (num1<num2):
    first=num2
    second=num1
else:
    print("both are equal")

#print(limit)
l=[]
for i in range(1,limit):
    for j in range(1,limit):
        if (second*j)==(first*i):
            l.append(second*j)
            
            break
        else:
            pass
        
print(l[0])









        
            
    



