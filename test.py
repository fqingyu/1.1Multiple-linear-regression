import numpy as np
from simple_linear_regression import SimpleLinearRegressionLine
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 5])

x_predict = 6
reg1 = SimpleLinearRegressionLine()
reg1.fit(x, y)

y_predict = reg1.predict(np.array([x_predict]))
print(y_predict)
print(reg1.a)
print(reg1.b)
y_hat = reg1.a * x + reg1.b

plt.scatter(x, y)
plt.plot(x, y_hat, color='r')
plt.axis([0, 7, 0, 7])
plt.show()
