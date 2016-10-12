import arff
import argparse
import numpy as np
from sklearn import tree
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

    y = np.squeeze(np.delete(data, range(0, 23), 1))
    X = np.delete(data, [23], 1)
    # y = np.squeeze(np.delete(data, range(0, 14), 1))
    # X = np.delete(data, [14], 1)
    attributes = [row[0] for row in arff_file['attributes']]
    del attributes[-1]

    clf = tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=2000, random_state=0,
                                      min_impurity_split=0.15)
    clf = clf.fit(X, y)
    scores = cross_val_score(clf, X, y, cv=10, n_jobs=-1, verbose=1)
    print clf.tree_.node_count
    # print num_leaves(clf.tree_)

    if output_file:
        with open(output_file, 'w') as f:
            tree.export_graphviz(clf, out_file=f)
    #
    # dot_data = tree.export_graphviz(clf, out_file=None,
    #                                 feature_names=arff_file['attributes'],
    #                                 class_names=['Target'],
    #                                 filled=True, rounded=True,
    #                                 special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dot_data)
    # Image(graph.create_png())

    print scores
    print("Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decision Tree Classifier using entropy')
    parser.add_argument('-i', dest='path', metavar='path', help='path for the datasource', required=True)
    parser.add_argument('-o', dest='output', help='the name of the output file')
    args = parser.parse_args()

    main(args.path, args.output)
