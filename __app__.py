import sys

if len(sys.argv) != 2:
    print("Usage should be: python scripts/script.py 'value1,value2,value3,...'")
    sys.exit(1)

input_string = sys.argv[1]
items = input_string.split(' ')

dir_to_be_removed = ['cicd']

res= []

for e in items:
    if e.startswith('.') or e.startswith('_') or e.startswith('README.md'):
        continue
    else:
        res.append(e.split('/')[0])

for e in dir_to_be_removed:
    if e in res:
        res.remove(e)

if not len(res):
    print('NO_BUILD')
else:
    print(' '.join(list(set(res))))
