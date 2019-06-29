obj=open("foo.txt")
a=obj.readlines()
print(a)

#reversing a list 
for c in range(len(a)):
	try :
		d=len(a)-c-1
		print(a[d])	
	except:
		print("ye case ni hua")
	obj1=open("roo.txt","a")
	obj1.write(a[d])


