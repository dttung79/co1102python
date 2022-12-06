import os


def index_and_list(dirname, root_path_length):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        if os.path.isdir(path):
            index_and_list(path, root_path_length)
        elif path.endswith(".py"):
            print(path[root_path_length:])


try:
    root_path = input("Enter the full path of the root directory\n (blank for current directory, .. for parent directory): ")
    if root_path == "":
        root_path = os.curdir
    elif root_path == "..":
        root_path = os.pardir
    if os.path.isdir(root_path):
        index_and_list(root_path, len(root_path) + 1)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")

print()
input("Press return to continue ...")
