import matplotlib.pyplot as plt
import os


def draw_graphic(data: list, filename: str, ylabel: str):
    plt.plot(data)
    plt.ylabel(ylabel)
    plt.savefig(filename)


def del_graphic(filename: str):
    os.remove(filename)