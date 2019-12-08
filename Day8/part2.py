with open('Input.txt') as f:
	data = [int(x) for x in f.read().strip()]

h=6
w=25

layers = [data[x:x+(h*w)] for x in range(0,len(data),h*w)]

out = [2 for y in range(h*w)]

for layer in reversed(layers):
	for i,val in enumerate(layer):
		if val != 2:
			out[i] = val

for x in range(h):
	l=''
	for y in range(w):
		l += '\033[1;30;40m ' if out[x*w+y]==0 else '\033[1;37;47m '
	l+='\033[0;30;40m'
	print(l)