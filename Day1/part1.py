fuel_required = 0
with open("Day1/Input.txt",'r') as f:
    for line in f.readlines():
        mass  = int(line)
        fuel_required += (mass//3)-2

print(fuel_required)