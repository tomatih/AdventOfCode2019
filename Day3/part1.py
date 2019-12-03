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

# go through all instructions
for direction, distance in path1:
	# horizontal
	if direction in ['R','L']:
		# create a line template and move cursor
		if direction == 'R':
			tmp = (current[0],current[0]+distance)
			current[0]+=distance
		else:
			tmp = (current[0]-distance,current[0])
			current[0]-=distance
		# add line to memory
		if current[1] in horizontal:
			horizontal[current[1]].append(tmp)
		else:
			horizontal[current[1]] = [tmp]
	
	# vertical
	if direction in ['U','D']:
		# create a line template and move cursor
		if direction == 'U':
			tmp = (current[1],current[1]+distance)
			current[1]+=distance
		else:
			tmp = (current[1]-distance,current[1])
			current[1]-=distance
		# add line to memory
		if current[0] in vertical:
			vertical[current[0]].append(tmp)
		else:
			vertical[current[0]] = [tmp]


#initialise data
current = [0,0]
intersections=list()

# go through all instructions
for direction, distance in path2:
	# horizontal
	if direction in ['R','L']:
		# create a line template and move cursor
		if direction == 'R':
			tmp = (current[0],current[0]+distance)
			current[0]+=distance
		else:
			tmp = (current[0]-distance,current[0])
			current[0]-=distance
		# check for collisions
		for i in range(tmp[0],tmp[1]+1):
			# horizontal lines collide with vertical
			# if crossing a coordinate with a vertical line
			if i in vertical:
				# check if colide
				for start,stop in vertical[i]:
					if current[1] > start and current[1] < stop:
						intersections.append((i,current[1]))

		
	
	# vertical
	if direction in ['U','D']:
		# create a line template and move cursor
		if direction == 'U':
			tmp = (current[1],current[1]+distance)
			current[1]+=distance
		else:
			tmp = (current[1]-distance,current[1])
			current[1]-=distance
		# check for collisions
		for i in range(tmp[0],tmp[1]+1):
			# horizontal lines collide with vertical
			# if crossing a coordinate with a vertical line
			if i in horizontal:
				# check if colide
				for start,stop in horizontal[i]:
					if current[0] > start and current[0] < stop:
						intersections.append((current[0],i))

out = -1
for x,y in intersections:
	distance = abs(x) + abs(y)
	if out == -1:
		out=distance
	if distance < out:
		out = distance

print(out)