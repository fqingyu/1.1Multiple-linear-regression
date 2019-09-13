import numpy as np
import random
from read_file import read_file

# y = ax1 + bx2
# theta[0]=a theta[1]=b
def gradient_descent(x, y, theta, alpha, max_iter):
    start_iter = 0
    m = x.shape[0]
    deviation = 0
    h = x.dot(theta)
    theta = theta + (alpha * np.array(x).T.dot(y - h))/m
    start_iter += 1
    for i in range(m):
        deviation += (y[i] - (x[i]).dot(theta)) ** 2
        # if deviation < 0.001 or start_iter >= max_iter:
        #     break

    # print(start_iter)
    # print(theta)
    return theta


def mini_batch_gd_by_matrix(max_data_num, mini_size, x, y, theta):
    index_array = range(0, max_data_num)
    index_array = np.array(index_array)
    index_array = np.random.permutation(index_array)
    print(index_array)
    for i in range(0, max_data_num, mini_size):
        mini_x = x[np.array(index_array[0:i+mini_size]), :]
        mini_y = y[np.array(index_array[0:i+mini_size]), :]
        theta = gradient_descent(x, y, theta, 0.05, max_iter)

    print(theta)
    return theta

try:
    max_data_num = 5
    mini_size = 1
    epoch_times = 5000
    x = np.array([[2.1, 1.5], [2.5, 2.3], [3.3, 3.9], [3.9, 5.1], [2.7, 2.7]])
    y = np.array([[2.5], [3.9], [6.7], [8.8], [4.6]])
    theta = np.array([[0], [0]])
    # x = read_file("kc_house_data.csv", ['bedrooms', 'floors', 'bathrooms', 'floors', 'condition', 'grade'], 10000)
    # y = read_file("kc_house_data.csv", ['price'], 10000)
    # theta = np.array([[3], [1], [1], [1], [3], [7]])

    alpha = 0.001
    max_iter = 10000
    # gradient_descent(x, y, theta, 0.05, max_iter)
    for i in range(epoch_times):
        theta = mini_batch_gd_by_matrix(max_data_num, mini_size, x, y, theta)
    print("********")
    print(theta)
    exit(0)
except Exception as e:
    print(e)
    exit(0)
