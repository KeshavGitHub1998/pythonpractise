#oops
'''
class bank():
    def __init__(self,name,mail):
        
        self.name=name
        self.mail=mail
        self.amount=0
        self.counter=0
        
        
       
    def withdrawl(self,amount):
        self.amount=self.amount-amount

    def deposit(self,amount):
        self.amount=self.amount+amount

    def display(self):
        print(self.amount)

obj=bank("keshav","keshav@gmail.com")
obj.deposit(3000)
obj.withdrawl(1500)
obj.display()'''
#----------------------------------------------------------------------------/#
'''class cal():
    a=10

obj=cal()
print(obj.a)'''

'''class school():

    def __init__(self,name,section,roll,percentage):
        self.name=name
        self.section=section
        self.roll=roll
        self.percentage=percentage
    def per(self):
        if self.percentage>=60:
            self.pers="First"
        print(self.name,self.roll,self.section,self.pers)   


obj=school("Testing","A",123,90)
obj.per()



obj1=school("Testing1","A",124,90)
obj1.per()




obj=school("Testing2","A",126,90)
obj.per()



obj=school("Testing3","A",123,90)
obj.per()'''


'''class person:
    def __init__(self,ik):
        self.ik=ik
        print("our class is created")
    def __del__(self):
        print("bahaut hua")
    def setfullname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname,"\n",self.lastname)


per=person(5)
per.setfullname("k","l")
per.printfullname()
per.__del__()
'''




'''class parent:
    value1="1"
    value2="2"

class child(parent):
    pass

objecto=parent()
childo=child()
print(childo.value1)'''

    
    
'''Create five functions in Class. To emlement stack(using list) in python.
1.	Push in stack (add item in stack).
2.	Pop in stack (remove item from stack).
3.	Display stack (show items of stack).
4.	Peek (to show top of stack).
5.	Exit (stop execution).
'''
class stack(self,k):
    def __init__(self,q,k):
        print("enter a value for the operation\n1.push\n2.pop\n3.display\n4.peek\n5.exit")
        
        self.q=q
        self.k=k
        
    def push(self,):
        
        print("enter a value in stack")
    def pop(self):
        



























