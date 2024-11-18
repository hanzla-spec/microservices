import sys

if len(sys.argv) != 3:
    print("Usage should be: python scripts/script.py 'branch_ref value1,value2,value3,....'")
    sys.exit(1)


print(sys.argv[1])

input_string = sys.argv[2]
items = input_string.split(' ')

res= []

for e in items:
    if e.startswith('.') or e.startswith('_'):
        continue
    else:
        res.append(e.split('/')[0])

if not len(res):
    print('NO_BUILD')
else:
    print(list(set(res)))