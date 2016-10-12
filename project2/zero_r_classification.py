import arff
import argparse
import numpy as np
from sklearn.dummy import DummyClassifier


def main(input_file, strategy):
    arff_file = arff.load(open(input_file, 'rb'))
    data = arff_file['data']

    y = np.squeeze(np.delete(data, range(0, 23), 1))
    X = np.delete(data, [23], 1)

    dummy_classifier = DummyClassifier(strategy=strategy)
    dummy_classifier.fit(X, y)
    print dummy_classifier.score(X, y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Zero R (Majority Class) Classifier')
    parser.add_argument('-i', dest='path', metavar='path', help='path for the datasource', required=True)
    parser.add_argument('--strategy', dest='strategy', metavar='strategy', help='strategy to use for the classifier')
    args = parser.parse_args()

    main(args.path, args.strategy or 'most_frequent')
