with open('Input.txt') as f:
	data = [int(x) for x in f.read().strip()]

h=6
w=25

layers = [data[x:x+(h*w)] for x in range(0,len(data),h*w)]

layer_d = dict()

min_z = h*w + 1 

for layer in layers:
	z_len = layer.count(0)
	layer_d[z_len] = layer.count(1) * layer.count(2)
	if z_len < min_z:
		min_z = z_len

print(layer_d[min_z])