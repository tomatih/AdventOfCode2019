with open('Input.txt','r') as f:
	data = [int(x) for x in f.read().strip().split(',')]


i=0
while 1:
	#print(i)
	tmp = str(data[i])
	opcode = int(tmp[-2:])
	param_modes = tmp[:-2]
	if opcode == 99:
		break
	elif opcode == 1:
		param_modes = '0'*(3-len(param_modes)) + param_modes
		a = data[i+1] if param_modes[-1]=='1' else data[data[i+1]]
		b = data[i+2] if param_modes[-2]=='1' else data[data[i+2]]
		if param_modes[0] == '0':
			data[data[i+3]] = a+b
		else:
			print('Scream for help')
			quit()
		i+=4
	elif opcode == 2:
		param_modes = '0'*(3-len(param_modes)) + param_modes
		a = data[i+1] if param_modes[-1]=='1' else data[data[i+1]]
		b = data[i+2] if param_modes[-2]=='1' else data[data[i+2]]
		if param_modes[0] == '0':
			data[data[i+3]] = a*b
		else:
			print('Scream for help')
			quit()
		i+=4
	elif opcode == 3:
		data[data[i+1]] = 1
		i+=2
	elif opcode == 4:
		param_modes = '0'*(1-len(param_modes)) + param_modes
		if param_modes[0]=='0':
			print(data[data[i+1]])
		else:
			print(data[i+1])
		i+=2
	else:
		print("Wrong opcode",opcode,tmp,i)
		quit()

		