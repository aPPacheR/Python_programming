
def print_hi(name, file):
    with open(file, 'w') as f:
        f.write(f'Hi, {name}')
    return file