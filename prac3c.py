
def prac():
	list= ' '
	alphabet=[
	[1,0,0,0,0,0,1],
	[1,0,0,0,0,0,1],
	[1,1,1,1,1,1,1],
	[1,0,0,0,0,0,1],
	[1,0,0,0,0,0,1]]
	for x, out in enumerate(alphabet):
		for y, inner in enumerate(out):
			if inner == 1:
				alphabet[x][y] = '*'
			if inner == 0:
				alphabet[x][y] = " "
	for n in range(0,5):
			print(*alphabet[n],sep=" ")

prac()
