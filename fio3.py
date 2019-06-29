def charcount(filename):
	return print(len(open(filename).read()))

charcount("foo.txt")