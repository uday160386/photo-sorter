# PhotoSorter
Utilities to sort photos by facial recognition, remove duplicates and identify the quality of photos. 

Install:

After cloning this repository, install required packages using the below command.

  
    python3 install -r requirements.txt

Utilities:

RemoveDuplicates: This utility will remove all the duplicate photos from given folder path.

    python RemoveDuplicatePhotos.py --path <Give the path to folder which contains a duplicate images>
   
   
ImageQualityIdentifier: This utility will help to know about the quality of a image on a scale of 0-100%
    
    python ImageQualityIdentifier.py --path <Give the path to folder which contains a images>
    
    
PhotosByFacialRecognition: This utility will help to identify the similar photos from a group of photos. It internally                                    used face_recognization.
      
      python PhotosByFacialRecognition.py --trainedPath <Give path to the folder with selected photos for training purpose>
                                          --sourcePath <Give path to the folder with photos which need to be identified>
