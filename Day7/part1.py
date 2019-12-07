# defining computer basics
with open('Input.txt','r') as f:
	raw_data = [int(x) for x in f.read().strip().split(',')]
i=0

#initialise day variables
inputs = list()
outputs=list()
data=list()

# helper function
def prepare_params(param_modes: str, p_len: int):
	params = list()
	for j in range(1, p_len+1):
		val = data[i+j] if param_modes%10 else data[data[i+j]]
		params.append(val)
		param_modes//=10
	return params 

# opcode functions
def jump_if_true(a,b):
	global i
	if a!=0:
		i = b-3

def jump_if_false(a,b):
	global i
	if a==0:
		i = b-3

def op_input():
	global inputs
	tmp = inputs[0]
	inputs=inputs[1:]
	return tmp


# instruction register
opcodes = {
	# sheme
	# opcode : (param_len: int, is_writing_to_memory: bool, function)
	1:(2,True, lambda a,b : a+b), # addition
	2:(2,True, lambda a,b : a*b), # multiplication
	3:(0,True, 	op_input), # input
	#4:(1,False, output),	# output
	5:(2,False, jump_if_true), # jump-if-true
	6:(2,False, jump_if_false), # jump-if-false
	7:(2,True, lambda a,b : 1 if a<b else 0),	# less than
	8:(2,True, lambda a,b : 1 if a==b else 0),	# equals
	99:(0,False, quit)
}

def run_intcomp():
	global i
	global data
	i=0
	data = raw_data[:]
	# main loop
	while 1:
		# get data 
		opcode = data[i]%100
		param_modes = (data[i] - opcode)//100
		# use data
		if opcode in opcodes:
			params = prepare_params(param_modes,opcodes[opcode][0]) # get params
			# if a return type
			if opcodes[opcode][1]:
				data[data[i+opcodes[opcode][0]+1]] = opcodes[opcode][2](*params)
			else:
				opcodes[opcode][2](*params)
			# static pointer movement
			i+=1 # intruction space
			i+=opcodes[opcode][0] # parameter spaces
			i+= 1 if opcodes[opcode][1] else 0 # return type space
		elif opcode == 4:
			params = prepare_params(param_modes,1)
			return params[0]
		else:
			print("Wrong opcode",opcode,tmp,i)
			quit()

# brute the  phases
for a in range(5):
	inputs = [a,0]
	ret_a = run_intcomp()

	for b in range(5):
		# filter repetitions
		if b==a:
			continue
		# run the phase
		inputs = [b, ret_a]
		ret_b = run_intcomp()

		for c in range(5):
			if c in [a,b]:
				continue

			inputs = [c, ret_b]
			ret_c = run_intcomp()

			for d in range(5):
				if d in [a,b,c]:
					continue

				inputs = [d, ret_c]
				ret_d = run_intcomp()

				for e in range(5):
					if e in [a,b,c,d]:
						continue
					inputs = [e, ret_d]
					ret_e = run_intcomp()
					# save output
					outputs.append(ret_e)

print(max(outputs))
