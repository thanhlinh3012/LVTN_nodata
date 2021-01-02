import sys

sys.path.append(".")

from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import time

start_time = time.time()
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True)
ap.add_argument("-i", "--index", required=True)
args = vars(ap.parse_args())
# initialize the color descriptor
#cd = ColorDescriptor((8, 12, 3))
cd = ColorDescriptor((24, 6, 6))  # 24bins for Hue chanel, 6bins for saturation chanel, 6bins for value chanel
# open the output index file for writing
output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	# describe the image
	features = cd.describe(image)
	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
	#cv2.waitKey(1000)
# close the index file
output.close()
print("%s seconds" % (time.time()-start_time))
