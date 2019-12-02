with open('Input.txt','r') as f:
	data = [int(x) for x in f.read().strip().split(',')]

data[1]=12
data[2]=2

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
		quit()

print(data[0])