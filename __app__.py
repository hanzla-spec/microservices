import sys

OUTPUT = ''

if len(sys.argv) != 2:
    sys.exit(1)

try:

    input_string = sys.argv[1]
    items = input_string.split(' ')

    dirs_to_be_ignored = ['cicd']

    apps_to_build = set()

    for item in items:
        if item.startswith('.') or item.startswith('_') or item.startswith('README.md'):
            continue
        else:
            app = item.split('/')[0]
            if app:
                apps_to_build.add(app)

    for item in dirs_to_be_ignored:
        if item in apps_to_build:
            apps_to_build.remove(item)

    OUTPUT = ' '.join(apps_to_build)

except ex:
    OUTPUT = ''

print(OUTPUT)
