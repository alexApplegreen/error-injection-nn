from datetime import datetime

from tensorflow.keras import layers, models
import numpy as np

from NEBULA.core import Injector, LegacyInjector

SAMPLESIZE = 5  # Modify this to set number of measurements
COUNTER = 0

if __name__ == "__main__":
    model = models.Sequential([
        # Input layer: assumes input shape of (128,) for example
        layers.Dense(256, activation='relu', input_shape=(128,)),  # 256 * (128 + 1) = 33,024 parameters
        # Second hidden layer
        layers.Dense(512, activation='relu'),  # 512 * (256 + 1) = 131,584 parameters
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        # Output layer
        layers.Dense(10, activation='softmax')  # 10 * (512 + 1) = 5,130 parameters
    ])

    model.summary()

    times_nebula = list()
    injector = Injector(model.layers)
    for i in range(SAMPLESIZE):

        time_start = datetime.now()
        injector.injectError(model)
        time_end = datetime.now()

        time = time_end - time_start
        times_nebula.append(time.microseconds)
        print(f"{time.microseconds}")

    times_legacy = list()
    injector = LegacyInjector(model.layers)
    for i in range(SAMPLESIZE):

        time_start = datetime.now()
        injector.injectError(model)
        time_end = datetime.now()

        time = time_end - time_start
        times_legacy.append(time.microseconds)
        print(f"{time.microseconds}")

    avg_nebula = np.average(np.asarray(times_nebula))
    avg_legacy = np.average(np.asarray(times_legacy))

    print(f"Nebula: {avg_nebula / 1000} ms, Legacy: {avg_legacy / 1000} ms")
