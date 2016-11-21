import csv
import argparse
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt


def read_csv_file():
    X = None
    labels = None
    count = 0

    with open(args.input_file, 'rb') as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:

            if count == 0:
                labels = row
            else:
                if X is None:
                    X = np.array([row])
                else:
                    X = np.append(X, [row], axis=0)

            count += 1

    return X, labels


def cluster_data():
    X, header_row = read_csv_file()
    labels_true = np.squeeze(np.delete(X, range(0, len(X[0]) - 1), 1))
    # X = np.delete(X, [20], 1)

    eps = float(args.eps) if args.eps else 0.3
    min_samples = int(args.n_samples) if args.n_samples else 10

    X = StandardScaler().fit_transform(X)
    # X = scale(X)
    reduced_data = PCA(n_components=2).fit_transform(X)

    db = DBSCAN(eps=eps, min_samples=min_samples).fit(reduced_data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    print labels

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f"
          % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f"
          % metrics.adjusted_mutual_info_score(labels_true, labels))
    # print("Silhouette Coefficient: %0.3f"
    #       % metrics.silhouette_score(X, labels))

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'

        class_member_mask = (labels == k)

        xy = reduced_data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


parser = argparse.ArgumentParser(description='Generate k clusters using the k-means clustering algorithm.')
parser.add_argument('-i', dest='input_file', metavar='input_file', help='path for the input file', required=True)
parser.add_argument('-eps', dest='eps', metavar='eps', help='The radius')
parser.add_argument('-n', dest='n_samples', metavar='n_samples', help='The number of samples')
args = parser.parse_args()
cluster_data()
