import argparse
import os
import sys

reverse = False
parser = argparse.ArgumentParser(description="Enter a non-empty root directory")
parser.add_argument("root", help="You must enter a root directory")

args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
    exit(-1)
else:
    file_format = input("Enter file format: ") or ""
    while True:
        print("Size sorting options:")
        print("1. Descending")
        print("2. Ascending")
        sort = int(input("Enter a sorting option "))
        if sort == 1:
            reverse = True
            break
        elif sort == 2:
            break
        else:
            print("Wrong option!")
            continue
    directory = args[1]
    file_storage = dict()
    for root, dirs, files in os.walk(directory):  # First, I get each file
        hash_key = 1  # The hash_key makes it so I can have duplicate sizes in the dictionary
        for name in files:
            file = os.path.basename(name)
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            if file_format == "":  # Print every file if file_format is blank
                file_storage[file_size + hash_key] = [file_path, hash_key]
            elif file[file.index(".") + 1:] == file_format:  # Print certain files if user wants certain format
                file_storage[file_size + hash_key] = [file_path, hash_key]
            hash_key += 1

    same_size = list()
    seen = list()
    no_same_files = True
    print(file_storage)
    for key, temp in file_storage.items():  # Now we loop through each file and see which ones are the same
        size_compare = int(key) - int(temp[1])
        for size_, value in file_storage.items():  # This one compares each file to the size_compare file for size
            if int(size_) - int(value[1]) == size_compare and value[0] not in same_size and value[0] not in seen:
                same_size.append(value[0])  # Add the file to same_size if it is the same size and we have not seen it
                seen.append(value[0])
        if len(same_size) > 1:  # Only if there are at least 2 files of same size we print them
            print("\n" + str(size_compare) + " bytes")
            no_same_files = False
            if reverse:
                list.reverse(same_size)
            for file in same_size:
                print(file)
        same_size.clear()
    if no_same_files:
        print("\nNo files with same size!")
