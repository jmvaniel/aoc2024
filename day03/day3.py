import re

def find_mul(value):
    pattern = re.compile('mul\(\d+,\d+\)')
    results = pattern.findall(value)
    totals = []
    for result in results:
        a, b = result.replace('mul(', '').replace(')', '').split(',')
        totals.append(int(a)*int(b))
    return totals

with open('input.txt', 'r') as f:
    test_input = f.read()

print sum(find_mul(test_input))

part_2_totals = []
do_statements = test_input.split('do()')
for do in do_statements:
    part_2_totals.append(sum(find_mul(do.split('don\'t()')[0])))

print sum(part_2_totals)
