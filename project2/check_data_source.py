import csv

with open('../default of credit card clients.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile);
    count = 0
    pay_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sex_values = [1, 2]
    education_values = [1, 2, 3, 4]
    marriage_values = [1, 2, 3]
    target_values = [0, 1]

    inv_education_values = []
    inv_marriage_values = []
    inv_pay_values = []
    inv_target_values = []

    for row in reader:
        if int(row['X2']) not in sex_values:
            print(count, row['X2'])

        if int(row['X3']) not in education_values:
            if int(row['X3']) not in inv_education_values:
                inv_education_values.append(int(row['X3']))

        if int(row['X4']) not in marriage_values:
            if int(row['X4']) not in inv_marriage_values:
                inv_marriage_values.append(int(row['X4']))

        if int(row['X5']) < 20:
            print(count, ' Age is less than 20: ', row['X5'])

        if int(row['X6']) not in pay_values:
            if int(row['X6']) not in inv_pay_values:
                inv_pay_values.append(int(row['X6']))

        if int(row['X7']) not in pay_values:
            if int(row['X7']) not in inv_pay_values:
                inv_pay_values.append(int(row['X7']))

        if int(row['X8']) not in pay_values:
            if int(row['X8']) not in inv_pay_values:
                inv_pay_values.append(int(row['X8']))

        if int(row['X9']) not in pay_values:
            if int(row['X9']) not in inv_pay_values:
                inv_pay_values.append(int(row['X9']))

        if int(row['X10']) not in pay_values:
            if int(row['X10']) not in inv_pay_values:
                inv_pay_values.append(int(row['X10']))

        if int(row['X11']) not in pay_values:
            if int(row['X11']) not in inv_pay_values:
                inv_pay_values.append(int(row['X11']))

        if int(row['X18']) < 0:
            print(count, ' X18 pay amount is incorrect: ', row['X18'])

        if int(row['X19']) < 0:
            print(count, ' X19 pay amount is incorrect: ', row['X19'])

        if int(row['X20']) < 0:
            print(count, ' X20 pay amount is incorrect: ', row['X20'])

        if int(row['X21']) < 0:
            print(count, ' X21 pay amount is incorrect: ', row['X21'])

        if int(row['X22']) < 0:
            print(count, ' X22 pay amount is incorrect: ', row['X22'])

        if int(row['X23']) < 0:
            print(count, ' X23 pay amount is incorrect: ', row['X23'])

        if int(row['Y']) not in target_values:
            if int(row['Y']) not in inv_target_values:
                inv_target_values.append(int(row['Y']))

        count += 1

    if inv_education_values:
        print('Invalid Education values:')
        for ed in inv_education_values:
            print(ed)

    if inv_marriage_values:
        print('Invalue Marriage values:')
        for m in inv_marriage_values:
            print(m)

    if inv_pay_values:
        print('Invalid Pay values:')
        for p in inv_pay_values:
            print(p)

    if inv_target_values:
        print('Invalid Target values')
        for t in inv_target_values:
            print(t)
