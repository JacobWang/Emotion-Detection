# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:39:23 2023

@author: Zhengqi Wang
"""

import matplotlib.pyplot as plt
import pandas as pd

def read_label_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        labels = file.read().splitlines()
    return {str(i): label for i, label in enumerate(labels)}

def process_tsv_file(filename, label_dict):
    label_counts = {label: 0 for label in label_dict.values()}
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            sentence, label_nums, nonew = line.strip().split('\t')
            labels = label_nums.split(',')
            for num in labels:
                if num in label_dict:
                    label_counts[label_dict[num]] += 1
    return label_counts

def plot_histogram(label_counts, title):
    labels, counts = zip(*label_counts.items())
    plt.bar(labels, counts)
    plt.xlabel('Labels')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()

def main():
    label_dict = read_label_file('labels.txt')

    files = ['dev.tsv', 'train.tsv', 'test.tsv']
    total_counts = {label: 0 for label in label_dict.values()}

    for file in files:
        counts = process_tsv_file(file, label_dict)
        for label, count in counts.items():
            total_counts[label] += count

    plot_histogram(total_counts, 'Label Distribution Across Datasets')

if __name__ == "__main__":
    main()