# Read a simple file
# autor - Ianara Fernandes

FILENAME = 'data.text'
DATADIR = '../datafile/'
print(DATADIR + FILENAME)
with open(DATADIR + FILENAME, 'rt') as fp:
    total = 0
    for line in fp:
        total += int(line.strip())  # Use strip() to remove any leading/trailing whitespace
        print(f'{line.strip()} is size {len(line.strip())}')  # Corrected the f-string
    print('')
    print(f'total is {total}')  # Corrected the f-string
