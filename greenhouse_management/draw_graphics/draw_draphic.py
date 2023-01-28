from typing import List

import matplotlib.pyplot as plt
import os


def draw_graphic(data: List[list], filename: str, suptitle: str, graphic_count):
    fig, axs = plt.subplots(nrows=graphic_count, ncols=1)

    fig.suptitle(suptitle)

    for i, item in enumerate(data):
        axs[i].plot(item)

    plt.savefig(filename)


def draw_grid_graphics(data: List[list], filename: str, suptitle: str, rows_count, cols_count):
    fig, axs = plt.subplots(nrows=rows_count, ncols=cols_count)

    fig.suptitle(suptitle)

    index = 0
    for row in range(rows_count):
        for col in range(cols_count):
            axs[row, col].plot(data[index])
            index += 1

    plt.savefig(filename)


def del_graphic(filename: str):
    os.remove(filename)