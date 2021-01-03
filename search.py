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

cd = ColorDescriptor((8, 12, 3))
#cd = ColorDescriptor((24, 6, 6))
query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
result = searcher.search(features)

print("Time to calculate eu distance: %s s \n" % (time.time()-start_time_eu))
start_time = time.time()
im_shape = (250, 250)
query_resized = cv2.resize(query, im_shape)
#cv2.imshow("query", query_resized)
plt.figure("Query")
plt.imshow(query_resized)
plt.axis("off")
results = []

plt.figure("Results", figsize=(3 * 3.13, 2 * 3.13))
#fig.add_subplot(3, 3, 1)
plt.subplots_adjust(hspace=0.4)
for (i, (score, resultID)) in enumerate(result):
    #result = cv2.imread(args["result_path"] + "/" + resultID)
    result = cv2.imread((args["result_path"] + resultID.replace('dataset', '')).replace('\\', '/'))
    results.append(result)
    """plt.subplot(1, len(results), i + 1)
    plt.title("{}: {:.2f}".format(resultID, score))
    plt.imshow(result)
    plt.axis("off")"""

    #cv2.imshow("result", result)
    #print(resultID)
    #print("%s seconds" % (time.time() - start_time))
    #cv2.waitKey(1000)
    #im_shape = (300, 300)
    #montage_shape = (3, 3)
    #montages = build_montages(results, im_shape, montage_shape)
    #for montage in montages:
    print(resultID)
    print(score)
    print("%s seconds" % (time.time() - start_time))
        #cv2.imshow("Result", montage)

    #for i in range(1, 10):
        #i = i + 1
    plt.subplot(3, 3, i + 1)

    plt.imshow(result)
    plt.title("{}: {:.2f}".format(resultID, score), fontdict={'fontsize': 6})

    #plt.show()

            #plt.axis("off")

        #cv2.waitKey(1000)
plt.show()

#print("%s seconds" % (time.time()-start_time))
cv2.waitKey(20000)
cv2.destroyAllWindows()

