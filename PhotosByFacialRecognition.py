import argparse
import os

import face_recognition
import shutil


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        if entry == '.DS_Store':
            os.remove(os.path.join(dirName, entry))
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def sort_photos(trainingpath, sourcepath):
    training_images = []

    trainingFiles = getListOfFiles(trainingpath)
    c = 0
    for file in trainingFiles:

        picture_of_me = face_recognition.load_image_file(file)
        try:
            if c <= 100:
                face_encoding = face_recognition.face_encodings(picture_of_me)[0]
                training_images.append(face_encoding)
                print("correct image: {}".format(c))
                c += 1
        except Exception as e:
            print(e)

    listOfFiles = getListOfFiles(sourcepath)

    for file in listOfFiles:
        picture_of_me = face_recognition.load_image_file(file)
        try:
            picture_encoding = face_recognition.face_encodings(picture_of_me)[0]

            results = face_recognition.compare_faces(training_images, picture_encoding)

            for result in results:
                if result:
                    shutil.copy(file, '{}'.format(sourcepath+'/after_sorting/'))
                    print("{} is a match!".format(file))
                else:
                    print("{} is a not match!".format(file))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set the path of images')
    parser.add_argument('--trainedPath', required=True)
    parser.add_argument('--sourcePath', required=True)

    args = parser.parse_args()
    sort_photos(args.trainedPath, args.sourcePath)
