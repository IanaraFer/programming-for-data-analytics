# Read a simple file
# autor - Ianara Fernandes

FILENAME = 'data.text'
DATADIR = '../datafile/'
print(DATADIR + FILENAME)
with open(DATADIR + FILENAME, 'rt') as fp:
    total = 0
    for line in fp:
        total += int(line)
        print(f'(line) is size {len(line)}')
    print('')
    print(f'total i {total}')
