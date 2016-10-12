import arff
import argparse
import numpy as np
from sklearn import tree
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.model_selection import cross_val_score


def num_leaves(my_tree):
    count = 0
    if my_tree.children_left is None and my_tree.children_right is None:
        return 1
    if my_tree.children_left.any():
        count += num_leaves(my_tree.children_left)
    if my_tree.children_right.any():
        count += num_leaves(my_tree.children_right)

    return count


def main(input_file, output_file):
    arff_file = arff.load(open(input_file, 'rb'))
    data = arff_file['data']

    rng = range(0, 11)
    rng.extend(range(12, 24))

    y = np.squeeze(np.delete(data, rng, 1))
    X = np.delete(data, [11], 1)

    # rng = range(0, 22)
    # rng.append(23)

    # y = np.squeeze(np.delete(data, rng, 1))
    # X = np.delete(data, [22], 1)
    # attributes = [str(row[0]) for row in arff_file['attributes']]
    # del attributes[-1]
    #
    clf = tree.DecisionTreeRegressor(min_samples_split=1500, random_state=0, max_depth=6)
    clf = clf.fit(X, y)
    scores = cross_val_score(clf, X, y, cv=10, n_jobs=-1, verbose=1)
    y_pred = clf.predict(X)

    if output_file:
        with open(output_file, 'w') as f:
            tree.export_graphviz(clf, out_file=f,
                                 feature_names=['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2',
                                                'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'PB_AMT1', 'PB_AMT2', 'PB_AMT3',
                                                'PB_AMT4', 'PB_AMT5', 'target'])



    print metrics.classification_report(y, y_pred)
    print 'Scores: ', scores
    print("Accuracy: %0.6f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
    print("Root Mean Squared Error: %0.6f" % (np.math.sqrt(mean_squared_error(y, y_pred))))
    print("Number of nodes %0.0f" % (clf.tree_.node_count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Regression Tree using entropy')
    parser.add_argument('-i', dest='path', metavar='path', help='path for the datasource', required=True)
    parser.add_argument('-o', dest='output', help='the name of the output file')
    args = parser.parse_args()

    main(args.path, args.output)
