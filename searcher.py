import numpy as np
import csv
from scipy.spatial import distance
from math import *

class Searcher:
    def __init__(self, indexPath):
        self.indexPath = indexPath

    def search(self, queryFeatures, limit=9):
        results = {}

        # open the index file for reading
        with open(self.indexPath) as f:
            reader = csv.reader(f)

            output = open("euclidean.csv", "w")
            for row in reader:
                # parse out the img ID & features
                # the compute the eu distance
                # between the features in our index & our query features
                features = [float(x) for x in row[1:]]
                d = self.eu_distance(features, queryFeatures)
                output.write("%s\n" % (str(d)))
                results[row[0]] = d     # distance between the 2 feature vectors
            f.close()
            output.close()
        out_results = open("results_sorted.csv", "w")
        # sort the results, the smaller distances are at the front of the list
        results = sorted([(v, k) for (k, v) in results.items()])
        out_results.write("%s\n" % (str(results)))
        out_results.close()
        return results[:limit]

    def eu_distance(self, histA, histB):
        #d = distance.euclidean(histA, histB)
        d = sqrt(sum(pow(a-b, 2) for a, b in zip(histA, histB)))
        return d


