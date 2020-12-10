from colordescriptor import ColorDescriptor
from searcher import Searcher
from imutils import build_montages
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True)
ap.add_argument("-q", "--query", required = True)
ap.add_argument("-r", "--result-path", required = True)
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
result = searcher.search(features)

cv2.imshow("Query", query)

results = []
for (score, resultID) in result:
    #result = cv2.imread(args["result_path"] + "/" + resultID)
    result = cv2.imread((args["result_path"] + resultID.replace('dataset', '')).replace('\\', '/'))
    #print((args["result_path"] + resultID.replace('dataset', '')).replace('\\', '/'))
    #cv2.imshow("Result", result)
    #cv2.waitKey(1000)
    results.append(result)
    im_shape = (300, 300)
    montage_shape = (5, 2)
    montages = build_montages(results, im_shape, montage_shape)
    for montage in montages:
        cv2.imshow("Result", montage)
        cv2.waitKey(1000)

cv2.waitKey(50000)
cv2.destroyAllWindows()
