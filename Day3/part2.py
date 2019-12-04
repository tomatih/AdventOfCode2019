# get data
with open('Input.txt','r') as f:
	path1, path2 = f.read().strip().split('\n')


# parse data
path1 = [ (x[0], int(x[1:])) for x in path1.split(',') ]
path2 = [ (x[0], int(x[1:])) for x in path2.split(',') ]



# initialise data
vertical = dict()
horizontal = dict()

# dict element structure
# [ (start_coordinate, step_indicator), (end_cordinate, step_indicator) ]

cursor = [0,0] # [x,y]
steps=0

# cinstruct first cable data
for direction, distance in path1:
	# vertical movement
	if direction in ['R','L']:
		# create data templates and move cursor
		if direction == 'R':
			template = (
				(cursor[0],steps),
				(cursor[0]+distance,-1)
			)
			cursor[0]+=distance
		else:
			template = (
				(cursor[0]-distance,-1),
				(cursor[0],steps)
			)
			cursor[0]-=distance
		# add steps
		steps+=distance
		# add to dict
		if cursor[1] in horizontal:
			horizontal[cursor[1]].append(template)
		else:
			horizontal[cursor[1]] = [template]

	# horizontal movement
	if direction in ['U','D']:
		# create data templates and move cursor
		if direction == 'U':
			template=(
				(cursor[1],steps),
				(cursor[1]+distance,-1)
			)
			cursor[1]+=distance
		else:
			template=(
				(cursor[1]-distance,-1),
				(cursor[1],steps)
			)
			cursor[1]-=distance
		# add steps
		steps+=distance
		# add to dict
		if cursor[0] in vertical:
			vertical[cursor[0]].append(template)
		else:
			vertical[cursor[0]] = [template]



# second cable data clear
cursor = [0,0]
steps = 0
out = list()

for direction,distance in path2:
	# horizontal movement crossing vertical
	if direction in ['R','L']:
		for i in range(distance):
			# movement
			steps+=1
			cursor[0]+= 1 if direction=='R' else -1
			# collisons
			if cursor[0] in vertical:
				for start, stop in vertical[cursor[0]]:
					if cursor[1] > start[0] and cursor[1] < stop[0]:
						# 2nd cable in steps
						start_point = start if start[1]!=-1 else stop
						out.append(start_point[1]+abs(cursor[1]-start_point[0])+steps)


	# vertical movement crossing horizontal
	if direction in ['U','D']:
		for i in range(distance):
			# movement
			steps+=1
			cursor[1]+= 1 if direction=='U' else -1
			# collisions
			if cursor[1] in horizontal:
				for start, stop in horizontal[cursor[1]]:
					if cursor[0] > start[0] and cursor[0] < stop[0]:
						# 2nd cable in steps
						start_point = start if start[1]!=-1 else stop
						out.append(start_point[1]+abs(cursor[0]-start_point[0])+steps)

print(min(out))