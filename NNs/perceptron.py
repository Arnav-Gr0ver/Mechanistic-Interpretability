import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class Perceptron:
    def __init__(self, dim, bias=0.0, learning_rate=0.1):
        self.dim = dim
        self.bias = bias
        self.learning_rate = learning_rate
        self.weights = np.zeros(self.dim)
        self.history = []
    def predict(self, input_vec):
        z = np.dot(self.weights, input_vec) + self.bias
        return 1 if z > 0 else 0
    def fit(self, target_vec, target_out, epochs=10):
        for epoch in range(epochs):
            for x, y in zip(target_vec, target_out):
                y_pred = self.predict(x)
                error = y - y_pred
                self.weights += self.learning_rate * error * x
                self.bias += self.learning_rate * error
            self.history.append((self.weights.copy(), self.bias))


#and gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 0, 0, 1])

model = Perceptron(dim=2, bias=0.0, learning_rate=0.1)

print("Predictions before training:")
for i in range(len(X)):
    print(f"{X[i]} => {model.predict(X[i])}")

model.fit(X, y, epochs=10)

print("\nPredictions after training:")
for i in range(len(X)):
    print(f"{X[i]} => {model.predict(X[i])}")

def interactive_plot(X, y, history):
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(bottom=0.2)

    scatter_0 = ax.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='0', edgecolors='k')
    scatter_1 = ax.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='1', edgecolors='k')

    x_vals = np.linspace(-0.5, 1.5, 100)
    line, = ax.plot([], [], 'k--')

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_title("Decision Boundary at Epoch 1")
    ax.legend()

    ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
    slider = Slider(ax_slider, 'Epoch', 1, len(history), valinit=1, valstep=1)

    def update(epoch):
        w, b = history[int(epoch) - 1]
        if w[1] != 0:
            y_vals = -(w[0] * x_vals + b) / w[1]
            line.set_data(x_vals, y_vals)
        else:
            line.set_data([ -b / w[0] ] * 2, [-0.5, 1.5])
        ax.set_title(f"Decision Boundary at Epoch {int(epoch)}")
        fig.canvas.draw_idle()

    slider.on_changed(update)
    update(1)
    plt.show()

interactive_plot(X, y, model.history)
