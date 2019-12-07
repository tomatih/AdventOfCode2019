data = dict()
planet_list = dict()

with open('Input.txt','r') as f:
	for line in f.readlines():
		#get data
		line = line.strip()
		a,b = line.split(')')
		# remember objects
		if a not in planet_list:
			planet_list[a]=-1
		if b not in planet_list:
			planet_list[b]=-1
		# remember connections
		if a in data:
			data[a].append(b)
		else:
			data[a] = [b]
		if b in data:
			data[b].append(a)
		else:
			data[b] = [a]


def dfs(start,distance=-1):
	#print(planet_list)
	distance+=1
	planet_list[start] = distance
	if start in data:
		for children in data[start]:
			if planet_list[children] == -1:
				dfs(children,distance)



dfs('COM')

out = 0 

for p in planet_list:
	out += planet_list[p]

print(out)


