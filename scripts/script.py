import sys

if len(sys.argv) != 2:
    print("Usage should be: python scripts/script.py 'value1,value2,value3,...'")
    sys.exit(1)

input_string = sys.argv[1]
items = input_string.split(' ')

res= []

for e in items:
    if e.startswith('.'):
        continue
    else:
        res.append(e.split('/')[0])

print(list(set(res))[0])


