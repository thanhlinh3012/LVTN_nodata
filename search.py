from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
import time
import os
import matplotlib.pyplot as plt

start_time = time.time()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True)
ap.add_argument("-q", "--query", required=True)
ap.add_argument("-r", "--result-path", required=True)
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))
# cd = ColorDescriptor((18, 3, 3))
query = cv2.imread(args["query"])
features = cd.describe(query)
print(features)

searcher = Searcher(args["index"])
result = searcher.search(features)

#print("Time to calculate eu distance: %s s \n" % (time.time()-start_time_eu))
#start_time = time.time()
im_shape = (350, 350)
query_resized = cv2.resize(query, im_shape)
query_resized = cv2.cvtColor(query_resized, cv2.COLOR_BGR2RGB)
#cv2.imshow("query", query_resized)
plt.figure("Query", figsize=(3.13, 3.13))
plt.imshow(query_resized)
plt.axis("off")
results = []

plt.figure("Results", figsize=(3 * 3.13, 2 * 3.13))
plt.subplots_adjust(left=0.065, right=0.925, bottom=0.025, top=0.95, hspace=0.135, wspace=0.25)
for (i, (score, resultID)) in enumerate(result):
    result = cv2.imread((args["result_path"] + resultID.replace('dataset', '')).replace('\\', '/'))
    results.append(result)
    """plt.subplot(1, len(results), i + 1)
    plt.title("{}: {:.2f}".format(resultID, score))
    plt.imshow(result)
    plt.axis("off")"""

    '''print(resultID)
    print("%s seconds" % (time.time() - start_time))
    cv2.waitKey(1000)
    im_shape = (300, 300)
    montage_shape = (3, 3)
    montages = build_montages(results, im_shape, montage_shape)
    for montage in montages:
        cv2.imshow("Result", montage)'''

    plt.subplot(3, 3, i + 1)
    RGB_result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    #RGB_result_resized = cv2.resize(RGB_result, im_shape)
    plt.imshow(RGB_result)
    #plt.imshow(result)
    plt.title("{}: {:.2f}".format(resultID, score), fontdict={'fontsize': 6})
    plt.axis("off")

    print(resultID)
    print("Euclidean: ", score)
    print("Time: %s s" % (time.time() - start_time))

plt.show()
cv2.destroyAllWindows()

