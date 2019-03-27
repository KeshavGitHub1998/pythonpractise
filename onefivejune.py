Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
mystring="amity university"
>>> find.mystring('s')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    find.mystring('s')
NameError: name 'find' is not defined
>>> mystring.find("s")
12
>>> mystring.replace("amity","sharda")
'sharda university'
>>> print(mystring)
amity university
>>> len(mystring)
16
>>> mystring.upper()
'AMITY UNIVERSITY'
>>> mystring.lower()
'amity university'
>>> mystring.split(i)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mystring.split(i)
NameError: name 'i' is not defined
>>> mystring.split("i")
['am', 'ty un', 'vers', 'ty']
>>> mystring.isalpha()
False
>>> mystring.isdigit()
False
>>> mystring.isspace()
False
>>> keshav="  "
>>> keshav.isspace()
True
>>> damani=" damani "
>>> print(damani)
 damani 
>>> strip.damani()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    strip.damani()
NameError: name 'strip' is not defined
>>> damani.strip()
'damani'
>>> mystring.endswith('y')
True
>>> mystring.startswith('k')
False
>>> mystring=int(input("enter the value:"))
enter the value:31
>>> mystring +1
32
>>> prinnt(mystring)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    prinnt(mystring)
NameError: name 'prinnt' is not defined
>>> print(mystring)
31
>>> mystring +=1
>>> print(mystring)
32
>>> variable=str(input(enter string))
SyntaxError: invalid syntax
>>> variable=str(input(enter the character value))
SyntaxError: invalid syntax
>>> variable = str(input('enter the strng'))
enter the strngqwerty
>>> print(variable)
qwerty
>>> print("ur % is {}".format(98.33))
ur % is 98.33
>>> print('hello {2} hello again {1} {0}'.format(56,54.909090,'hello'))
hello hello hello again 54.90909 56
>>>  print('hello {2} hello again {1} {}'.format(56,54.909090,'hello'))
SyntaxError: unexpected indent
>>> print('hello {} hello again {1} {0}'.format(56,54.909090,'hello'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('hello {} hello again {1} {0}'.format(56,54.909090,'hello'))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print("year no is {0:.2f}".format(98.232341))
year no is 98.23
>>> print("ur age is{2.2f}".format(212434.12341412))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("ur age is{2.2f}".format(212434.12341412))
IndexError: tuple index out of range
>>> print("ur age{0:2.2f}".format(123411.412423143))
ur age123411.41
>>> print("ur age(0:>5.2.0f)".format(888898.5445))
ur age(0:>5.2.0f)
>>> print("ur age(0:<.2f)".format(55.5454))
ur age(0:<.2f)
>>>  print("ur age[0:<.2f}".format(55.5454))
SyntaxError: unexpected indent
>>>  print("ur age{0:<.2f}".format(55.5454))
SyntaxError: unexpected indent
>>> print("ur age{0:<.2f}".format(55.5454))
ur age55.55
>>> print("ur ph no{0:>.2f}".format(44.23))
ur ph no44.23
>>> print("ur ph no{0:^.0f}".format(44323.333333))
ur ph no44323
>>> print("ur ph no{0:^16.0f}".format(44323.333333))
ur ph no     44323      
>>> print("ur ph no{0:*^17.0f}".format(44323.333333))
ur ph no******44323******
>>>  dir(__builtins__)
SyntaxError: unexpected indent
>>> dir(__buitins__)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dir(__buitins__)
NameError: name '__buitins__' is not defined
>>> 
