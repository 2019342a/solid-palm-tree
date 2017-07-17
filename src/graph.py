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

def main():
    parsed_data = parse.parse(parse.SF_FILE, ",")
    visualize_days(parsed_data)

if __name__ == "__main__":
    main()
