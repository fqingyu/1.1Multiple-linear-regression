import numpy as np
import random


# y = ax1 + bx2
# theta[0]=a theta[1]=b
def gradient_descent(x, y, theta, alpha, m, iter, max_iter):
    while True:
        deviation = 0
        i = random.randint(0, m-1)
        h = theta[0] * x[i][0] + theta[1] * x[i][1]
        theta[0] += alpha * (y[i] - h) * x[i][0]
        theta[1] += alpha * (y[i] - h) * x[i][1]
        iter += 1
        for i in range(m):
            deviation = deviation + (y[i] - (theta[0] * x[i][0] + theta[1] * x[i][1])) ** 2
        if deviation < 0.0001 or iter > max_iter:
            break
        print(theta)

    print(iter)
    print(theta)

iter = 0
x = [[2.1, 1.5], [2.5, 2.3], [3.3, 3.9], [3.9, 5.1], [2.7, 2.7]]
y = [2.5, 3.9, 6.7, 8.8, 4.6]
theta = [2, -1]
alpha = 0.05
m = 5
max_iter = 10000
gradient_descent(x, y, theta, 0.05, 5, iter, max_iter)