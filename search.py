from colordescriptor import ColorDescriptor
from searcher import Searcher
from imutils import build_montages
import argparse
import cv2
import time
import matplotlib.pyplot as plt

start_time_eu = time.time()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True)
ap.add_argument("-q", "--query", required=True)
ap.add_argument("-r", "--result-path", required=True)
args = vars(ap.parse_args())

#cd = ColorDescriptor((8, 12, 3))
cd = ColorDescriptor((24, 6, 6))
query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
result = searcher.search(features)

print("Time to calculate eu distance: %s s \n" % (time.time()-start_time_eu))
start_time = time.time()
im_shape = (250, 250)
query_resized = cv2.resize(query, im_shape)
cv2.imshow("Query", query_resized)
#cv2.imshow("query", query)
results = []
for (score, resultID) in result:
    #result = cv2.imread(args["result_path"] + "/" + resultID)
    result = cv2.imread((args["result_path"] + resultID.replace('dataset', '')).replace('\\', '/'))
    results.append(result)
    #cv2.imshow("result", result)
    #print(resultID)
    #print("%s seconds" % (time.time() - start_time))
    #cv2.waitKey(1000)
    #im_shape = (300, 300)
    montage_shape = (3, 3)
    montages = build_montages(results, im_shape, montage_shape)
    for montage in montages:
        print(resultID)
        print(score)
        cv2.imshow("Result", montage)
        print("%s seconds" % (time.time()-start_time))
        #cv2.waitKey(1000)

cv2.waitKey(20000)
cv2.destroyAllWindows()

