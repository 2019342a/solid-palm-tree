"""
Module that stores the functions used for creating a graph.
"""

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

import parse

def visualize_days(parsed_data):
    """Visualize data by day of week"""

    counter = Counter(item["DayOfWeek"] for item in parsed_data)

    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
        ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(data_list)

    plt.xticks(range(len(day_tuple)), day_tuple)

    plt.savefig("Days.png")

    plt.clf()

def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""

    width = 0.5

    counter = Counter(item["DayOfWeek"] for item in parsed_data)

    labels = tuple(counter.keys())

    xlocations = np.arange(len(labels)) + 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width / 2, labels, rotation=90)

    plt.subplots_adjust(bottom=0.4)

    plt.rcParams['figure.figsize'] = 12, 8

    plt.savefig("Type.png")

    plt.clf()

def main():
    parsed_data = parse.parse(parse.SF_FILE, ",")
    visualize_type(parsed_data)

if __name__ == "__main__":
    main()
