f=open("foo.txt",'w')
f.write("b")
f.close()
f=open("foo.txt","r")
print(f.readline())
