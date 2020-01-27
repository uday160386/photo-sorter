# pip install image-quality
import imquality.brisque as brisque
import PIL.Image
import shutil

import os
import argparse


def sort_by_quality_of_image(path):
    file_list = os.listdir(path)
    for index, filename in enumerate(file_list):
        img = PIL.Image.open(path + '/' + filename)
        score = brisque.score(img)
        print('Score for image {} is {}'.format(filename, score))

        if 0 < score <= 10.0:

            if not os.path.exists(path+"/0-10"):
                os.makedirs(path + '/0-10')
                print("dir created@", path + '/0-10')
            shutil.copy(path + '/' + filename, path + '/0-10/' + filename)
        elif 10 < score <= 20.0:
            if not os.path.exists(path+"/10-20"):
                os.makedirs(path + '/10-20')
            shutil.copy(path + '/' + filename, path + '/10-20/' + filename)
        elif 20 < score <= 30.0:
            if not os.path.exists(path+"/20-30"):
                os.makedirs(path + '/20-30')
            shutil.copy(path + '/' + filename, path + '/20-30/' + filename)
        elif 30 < score <= 40.0:
            if not os.path.exists(path+"/30-40"):
                os.makedirs(path + '/30-40')
            shutil.copy(path + '/' + filename, path + '/30-40/' + filename)
        elif 40 < score <= 50.0:
            if not os.path.exists(path+"/40-50"):
                os.makedirs(path + '/40-50')
            shutil.copy(path + '/' + filename, path + '/40-50/' + filename)
        elif 50 < score <= 60.0:
            if not os.path.exists(path+"/50-60"):
                os.makedirs(path + '/50-60')
            shutil.copy(path + '/' + filename, path + '/50-60/' + filename)
        elif 60 < score <= 70.0:
            if not os.path.exists(path+"/60-70"):
                os.makedirs(path + '/60-70')
            shutil.copy(path + '/' + filename, path + '/60-70/' + filename)
        elif 70 < score <= 80.0:
            if not os.path.exists(path+"/70-80"):
                os.makedirs(path + '/70-80')
            shutil.copy(path + '/' + filename, path + '/70-80/' + filename)
        elif 80 < score <= 90.0:
            if not os.path.exists(path+"/80-90"):
                os.makedirs(path + '/80-90')
            shutil.copy(path + '/' + filename, path + '/80-90/' + filename)
        elif 90 < score <= 100.0:
            if not os.path.exists(path+"/90-100"):
                os.makedirs(path + '/90-100')
            shutil.copy(path + '/' + filename, path + '/90-100/' + filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set the path of images')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    sort_by_quality_of_image(args.path)
