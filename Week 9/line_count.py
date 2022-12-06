import os

def count_lines(fname):
    with open(fname) as f:
        return len(f.readlines())

dir_name = input('Enter directory name: ')
# read file names in the directory
file_names = os.listdir(dir_name)
try:
    for fname in file_names:
        # check if fname is not a directory
        if not os.path.isdir(dir_name + '/' + fname) and fname[0] != '.':
            print(fname, count_lines(dir_name + '/' + fname))
except UnicodeDecodeError:
    print('Error at file: ', fname)