# get data
with open('Input.txt','r') as f:
	path1, path2 = f.read().strip().split('\n')


# parse data
path1 = [ (x[0], int(x[1:])) for x in path1.split(',') ]
path2 = [ (x[0], int(x[1:])) for x in path2.split(',') ]

# create data holders
# dict with a scheme line in a named direction from a to b on cordinate key
horizontal = dict()
vertical = dict()

# initialise data
current = [0,0]
steps=0

# go through all instructions
for direction, distance in path1:
	# horizontal
	if direction in ['R','L']:
		# create a line template and move cursor
		if direction == 'R':
			tmp = ((current[0],steps),(current[0]+distance,-1))
			current[0]+=distance
		else:
			tmp = ((current[0]-distance,-1),(current[0],steps))
			current[0]-=distance
		steps+=distance
		# add line to memory
		if current[1] in horizontal:
			horizontal[current[1]].append(tmp)
		else:
			horizontal[current[1]] = [tmp]
	
	# vertical
	if direction in ['U','D']:
		# create a line template and move cursor
		if direction == 'U':
			tmp = ((current[1],steps),(current[1]+distance,-1))
			current[1]+=distance
		else:
			tmp = ((current[1]-distance,-1),(current[1],steps))
			current[1]-=distance
		steps+=distance
		# add line to memory
		if current[0] in vertical:
			vertical[current[0]].append(tmp)
		else:
			vertical[current[0]] = [tmp]


#initialise data
current = [0,0]
steps=0
intersections=list()


# go through all instructions
for direction, distance in path2:
	# horizontal
	if direction in ['R','L']:
		for i in range(distance):
			steps+=1
			current[0]+=1
			if current[0] in vertical:
				for start, stop in vertical[current[0]]:
					if current[0]< stop[0] and current[0]>start[0]:
						#calculate
						start_point = start if start[1]!=-1 else stop
						print(start_point[1],)
		
	
	# vertical
	if direction in ['U','D']:
		for i in range(distance):
			steps+=1
			current[1]+=1
			if current[1] in horizontal:
				for start, stop in horizontal[current[1]]:
					if current[1]< stop[0] and current[1]>start[0]:
						#calculate
						start_point = start if start[1]!=-1 else stop
						print(start_point[1],abs(current[1]-start_point[1]))
						

print(intersections)
