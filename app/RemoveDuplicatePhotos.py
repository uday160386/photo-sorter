import os
import argparse

duplicates = []


def delete_duplicate_images(path):
    file_list = os.listdir(path)
    print("Before deleting:", len(file_list))

    hash_keys = dict()
    for index, filename in enumerate(file_list):
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            if filehash not in hash_keys:
                hash_keys[filehash] = index
            else:
                duplicates.append((index, hash_keys[filehash]))

    for index in duplicates:
        os.remove(file_list[index[0]])

    print("After Sorting", len(file_list))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set the path of images')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    delete_duplicate_images(args.path)
