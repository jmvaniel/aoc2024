def check_values(values):
    return all(0 < values[i]-values[i+1] < 4 for i in range(len(values)-1)) or all(0 < values[i+1]-values[i] < 4 for i in range(len(values)-1))

def is_safe(values):
    return check_values(values)

def is_safe_after_dampening(values):
    if any(check_values(values[:i]+values[i+1:]) for i in range(len(values))):
        return True
    return False

# Part 1
with open('input.txt', 'r') as f:
    lines = f.readlines()

safe = 0
all_safe = 0

for line in lines:
    line = [int(x) for x in line.split()]
    print(line)
    if is_safe(line):
        safe += 1
        all_safe += 1
    elif is_safe_after_dampening(line):
        all_safe += 1
