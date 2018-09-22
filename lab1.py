import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []
    files = []

    # Your code goes here
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".jpg")]:
            files.append(os.path.join(dirpath, filename))
    for fil in files:
        if 'dog' in fil:
            dog_list.append(fil)
        elif 'cat' in fil:
            cat_list.append(fil)

    return cat_list, dog_list


def main():
    start_path = './' # current directory

    process_dir(start_path)
    print(process_dir(start_path))

main()
