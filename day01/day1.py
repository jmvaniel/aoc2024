from collections import Counter

# Day 1, Part 1
left, right = [], []
with open('input.txt') as f:
    for line in f.readlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left.sort()
right.sort()

print(sum(abs(left[i]-right[i]) for i in range(len(left))))

# Day 1, Part 2
counter = Counter(right)
print(sum(i*counter[i] for i in left))