def check(x):
	x = [ int(y) for y in str(x)]
	for i in range(len(x)-1):
		if x[i] > x[i+1]:
			return False
	if len(set(x)) == len(x):
		return False
	for a in set(x):
		if x.count(a)==2:
			return True
	return False
	
out=0
for i in range(367479,893698+1):
	out += 1 if check(i) else 0
	
print(out)