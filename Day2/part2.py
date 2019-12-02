data_raw=[]

with open('Input.txt','r') as f:
	data_raw = [int(x) for x in f.read().strip().split(',')]


def calculate(x: int, y: int):
	global data_raw
	data = [x for x in data_raw]
	data[1]=x
	data[2]=y

	i=0
	while 1:
		if data[i]==99:
			break
		elif data[i]==1:
			tmp = (data[data[i+1]],data[data[i+2]])
			data[data[i+3]] = sum(tmp)
			i+=4
		elif data[i]==2:
			a=data[data[i+1]]
			b=data[data[i+2]]
			data[data[i+3]] = a*b
			i+=4
		else:
			print("Scream for help!")
			return None

	return data[0]


for a in range(0,100):
	for b in range(0,100):
		if calculate(a,b) == 19690720:
			print("{}{}".format(a,b))