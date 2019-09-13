import csv
import numpy as np


def read_file(path, variables, max_data_num):
    variable_num = len(variables)
    matrix_x = np.zeros(shape=(0, variable_num))
    data_num = 0
    # if dimension == 1:
    #     matrix_x = np.zeros(shape=(0, 1))
    # elif dimension == 2:
    #     matrix_x = np.zeros(shape=(0, 2))
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_array = []
            for v in variables:
                new_array.append(float(row[v]))
            matrix_x = np.row_stack((matrix_x, new_array))
            data_num += 1
            if data_num >= max_data_num:
                break


    return matrix_x
    # print(matrix_x)
    exit(0)


# read_file("kc_house_data.csv", ['price'], 1)

# test = np.zeros(shape=(0, 2))
# # test = [[1,2]]
# test = np.append(test, [[1, 1]], axis=0)
# print(test)