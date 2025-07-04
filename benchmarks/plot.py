import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    layers = [3, 4, 5, 6, 7, 8, 9, 10]
    runtimes_legacy = [405.1, 410.319, 415.897, 419.3, 420.4, 512.1, 680.4, 812]  # in ms
    runtimes_nebula = [220.4, 289.785, 236.53, 240.6, 287.18, 294.17, 245, 253]  # in ms

    plt.plot(layers, runtimes_legacy, color='red', marker='x', label="Legacy")
    plt.plot(layers, runtimes_nebula, color='blue', marker='^', label="NEBULA")
    plt.xlabel("Number of layers")
    plt.ylabel("Runtime in ms")
    plt.legend()
    plt.show()
