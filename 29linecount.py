def linecount(filename):
	return print(len(open(filename).readlines()))

linecount("foo.txt")