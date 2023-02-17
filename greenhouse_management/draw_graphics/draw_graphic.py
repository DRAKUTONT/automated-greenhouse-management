from typing import List

import matplotlib.pyplot as plt
import os


def draw_graph_average_values(temp_data: list, hum_data: list, filename: str, value_count: int, time: int):
    plt.plot(temp_data, 'r', label='Средняя температура', lw=1)
    plt.plot(hum_data, 'b', label='Средняя влажность', lw=1)

    plt.xticks(ticks=list(range(value_count)), labels=list(range(time)))
    plt.grid()
    plt.legend(loc=2)
    plt.savefig(filename, bbox_inches='tight', dpi=900)
    plt.close()


def draw_sensors_graphics(sensors_data: List[list], filename: str, value_count: int, time: int):
    for i, item in enumerate(sensors_data):
        plt.plot(item, label=f'Датчик {i + 1}', lw=1)

    plt.xticks(ticks=list(range(value_count)), labels=list(range(time)))
    plt.grid()
    plt.legend(loc=2)
    plt.savefig(filename, bbox_inches='tight', dpi=900)
    plt.close()


def del_graphic(filename: str):
    os.remove(filename)