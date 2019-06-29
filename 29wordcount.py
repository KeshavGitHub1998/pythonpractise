def wordcount(filename):
	return print(len(open(filename).read().split()))

wordcount("foo.txt")