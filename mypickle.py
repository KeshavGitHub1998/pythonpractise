import os
import pickle
file=open("aa.txt","wb")
my={1998:['a'],1997:['b']}

pickle.dump(my,file)
file.close()
file=open("aa.txt","rb+")

a=pickle.load(file)
print(a)
