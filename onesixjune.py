print("creating a calculator")
print("enter the operation you want to run\(enter the serial number only\)")
print("1. addition  2. subtraction  3. multiplication")
q=int(input("enter you number here"))
num1=int(input("first number"))
num2=int(input("second number"))
if q==1:
    r=sum(num1,num2)
    print(r)
elif q==2:
    r=num1-num2
    print(r)
elif q==3:
    r=num1*num2
    print(r)
else :
    print("choose from given options!")

print("thank you for using my calculator") 
#-------------------------------
#PRIME NUMBER MACHINE
print("checking a prime number")
number=int(input("enter number"))
#if number %1 == 
if number > 1:
    for i in range (2,number):
        if (number %i)==0:
            print("number is not a prime")
            break
        else:
            print("{} is a prime".format(number))
            break
else:
    print("type a number greater than 1")

print("thank you for using prime number machine")
#---------------------------------------VOWEL COUNTING macHINE
print("finding the number of vowels")
string=input("enter the string without space")
count=0
for i in string:
    if(i=='a' or i=='i' or i=="e" or i=='o' or i=='u'):
        count+=1
    else:
       pass
       
print(count)
print("thank you for using vowel machine")
    

#-------------------------------------
#FACTORIAL OF A NUMBER (non exception handling)
#factorial of a number
print("enter the number ")
number=int(input("now"))
factorial=1
for i in range (1,number+1):
    factorial=i*factorial
print(factorial)
#------------
#QUADRATIC MACHINE FoR REAL ROOTs
import math
a=int(input("value for a "))
b=int(input("value for b "))
c=int(input("value for c "))
d=(b*b)-(4*a*c)
if d<0:
    print("imaginary roots")
else:
    sol1=(-b-math.sqrt(d))/(2*a)
    sol2=(-b+math.sqrt(d))/(2*a)
    print("{} & {} are solutions".format(sol1,sol2))
print("thank you for using quadratic machine")
    
#-----------------------------------
#SWAPPING MACHINE

#swapping machine
print("enter the numbers to be swapped one by one")
num1=int(input("num1"))
num2=int(input("num2"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("swapped numbers are {} and {}".format(num1,num2))
print("thank you for using swapping machine")

#-------------------------------------
#ODD EVEN 
#odd even number
print("enter the number ")
number=int(input("\n ?"))
if (number%2==0):
    print("even")
else :
    print("odd")
print("thank you for using the machine")

#------------------
#LEAP YEAR
#odd even number
print("enter the year ")
number=int(input("\n ?"))
if (number%4==0):
    print("leap")
else :
    print("non-leap")
print("thank you for using the machine")

#--------------------------------------
#PRIME numBERS FROM A RANGE
#finding prime numbers in a interval
print("enter the numbers in ascending order")
limit1=int(input("small value"))
limit2=int(input("big value"))
for i in range(limit1,limit2+1):
    for j in range(2,i):
         if (i%j ==0):
             print("number is not prime")
             print(i)
             break
    else:
        print("number is prime")
print("thank you for using prime number machine")
#------------------------------------

#table machine
#multiplication table
value=int(input("enter the table of number you want to see"))

for i in range(1,11):
    table=i*value
    print("{}*{}={}".format(i,value,table))
print("thank you for using table machine")
#---------------------------

#sum of natural numbers
number=int(input("enter the number you want sum till\n"))
trim=0
for i in range(1,number+1):
    trim+=i
print(trim)
#----------
#2 power machine
#display power of 2
print("displaying the power of 2")
for i in range(1,11):
    answer = 2**i
    print("2 to the power of {} is {}".format(i,answer))
print("thank you for using 2 power machine")
#------------------------------------
#decimal into binary
#predefined functions 
#-------------------
#PYTHON STYLE SWAP
a=int(input("enter value of a"))
b=int(input("enter value of b"))
a,b=b,a
print("{} is now a".format(b))
print("{} is now b".format(a))
#---------------------------------
#finding factorial
num=int(input("enter a number"))
for i in range(1,num):
    num*=i
print(num)
#---------------------------------

