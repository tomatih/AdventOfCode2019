fuel_required = 0

def fuel_calculator(amount: int):
    required = (amount//3)-2
    if(required >= 0):
        return required+fuel_calculator(required)
    else:
        return 0

with open("Day1/Input.txt",'r') as f:
    for line in f.readlines():
        mass  = int(line)
        fuel_required += fuel_calculator(mass)

print(fuel_required)