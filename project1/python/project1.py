__author__ = 'francisco'
import arff
import numpy as np
from sklearn.decomposition import PCA

data = arff.load(open('/Users/francisco/Google Drive/Education/WPI/CS 548 Knowledge Discovery and Data Mining/Project 1/CommViolPredUnnormalizedData-3.arff', 'rb'))
X = np.array(data['data'])
pca = PCA(copy=True, n_components=5, whiten=True)
pca.fit(X)
print(pca.explained_variance_ratio_)


