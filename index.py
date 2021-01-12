import argparse
import glob
import cv2
import time
import sys
from colordescriptor import ColorDescriptor
sys.path.append(".")

start_time = time.time()

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True)
ap.add_argument("-i", "--index", required=True)
args = vars(ap.parse_args())
# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))  # 8bins for Hue chanel, 12bins for saturation chanel, 3bins for value chanel

# open the output index file for writing
output = open(args["index"], "w")
for imagePath in glob.glob(args["dataset"] + "/*"):
	# extract the image ID from the image
	imageID = imagePath[imagePath.rfind("/") + 1:]
	# path and load the image itself
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


