import argparse
import Orange


def process_csv_file():
    data = Orange.data.Table(args.path)
    # data = Orange.data.Table("market-basket.basket")

    print("Attributes:", ", ".join(x.name for x in data.domain.attributes))
    print("Class:", data.domain.class_var.name)
    print("Data instances", len(data))

    rules = Orange.associate.AssociationRulesInducer(data, support=0.1, confidence=0.9, classification_rules=True)
    print "%2s %4s %4s %4s  %s" % ("Ix", "Supp", "Conf", "Rule", "Lift")
    count = 1
    for r in rules:
        print "%2.0f %4.3f %4.3f %4.3f  %s" % (count, r.support, r.confidence, r.lift, r)
        count += 1


parser = argparse.ArgumentParser(description='Build association rules from a dataset.')
parser.add_argument('-i', dest='path', metavar='path', help='path of the csv file', required=True)
args = parser.parse_args()
process_csv_file()

