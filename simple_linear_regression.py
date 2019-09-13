import numpy as np


# y = ax + b
class SimpleLinearRegressionLine:

    def __init__(self):
        self.a = None
        self.b = None

    def fit(self, x_train, y_train):
        assert x_train.ndim == 1
        assert len(x_train) == len(y_train)

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0

        num += (x_train-x_mean).dot(y_train-y_mean)
        d += (x_train-x_mean).dot(x_train-x_mean)
        self.a = num/d
        self.b = y_mean - self.a * x_mean

        return self

    def predict(self, x_predict):
        assert x_predict.ndim == 1
        assert self.a is not None and self.b is not None
        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        return self.a * x_single + self.b

    def __repr__(self):
        return "SimpleLinearRegression()"
