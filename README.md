import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np

def plot_linear_functions_intersection(func1, func2, func1_label, func2_label):
    x = np.linspace(-10, 10, 100)
    y1 = func1(x)
    y2 = func2(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Графики пересечения функций", fontsize=16)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax.plot(x, y1, c="red", label=func1_label)
    ax.plot(x, y2, label=func2_label)
    ax.legend()
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)

    plt.show()
