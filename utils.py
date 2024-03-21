from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def plot_throughput_latency_turnaround(results_1, results_2, results_1_title, results_2_title, figure_title):
    """
    def plot_throughput_latency_turnaround(results_1, results_2, results_1_title, results_2_title, figure_title):
    Plots the median latency, mean latency, and turnaround time by throughput for two sets of results.

    Args:
        results_1 (DataFrame): A DataFrame containing the first set of results. It should have columns 'Batch Size', 'Median Latency', 'Mean Latency', and 'Time Taken'.
        results_2 (DataFrame): A DataFrame containing the second set of results. It should have columns 'Batch Size', 'Median Latency', 'Mean Latency', and 'Time Taken'.
        results_1_title (str): The title to use for the first set of results in the legend.
        results_2_title (str): The title to use for the second set of results in the legend.
        figure_title (str): The title to use for the entire figure.

    Returns:
        None
    """
    fig, axs = plt.subplots(1, 3, figsize=(21, 7.5))
    
    axs[0].plot(results_1['Batch Size'], results_1['Median Latency'], label=results_1_title)
    axs[0].plot(results_2['Batch Size'], results_2['Median Latency'], label=results_2_title)
    axs[0].set_title('Median Latency by Throughput')
    axs[0].set_xlabel('Batch Size')
    axs[0].set_ylabel('Latency (s)')
    axs[0].set_ylim(0, max(results_1['Median Latency'].max(), results_2['Median Latency'].max())+1)
    axs[0].legend()
    
    axs[1].plot(results_1['Batch Size'], results_1['Mean Latency'], label=results_1_title, marker='.', markersize=1)
    axs[1].plot(results_2['Batch Size'], results_2['Mean Latency'], label=results_2_title, marker='p', markersize=1)
    axs[1].set_title('Mean Latency by Throughput')
    axs[1].set_xlabel('Batch Size')
    axs[1].set_ylabel('Latency (s)')
    axs[1].set_ylim(0, max(results_1['Mean Latency'].max(), results_2['Mean Latency'].max())+1)
    axs[1].legend()
    
    axs[2].bar(results_1['Batch Size'], results_1['Time Taken'], label=results_1_title, alpha=0.5)
    axs[2].bar(results_2['Batch Size'], results_2['Time Taken'], label=results_2_title, alpha=0.5)
    axs[2].set_title('Result turnaround by Throughput')
    axs[2].set_xlabel('Batch Size')
    axs[2].set_ylabel('Turnaround (s)')
    axs[2].set_ylim(0, max(results_1['Time Taken'].max(), results_2['Time Taken'].max())+1)
    axs[2].legend()
    
    # Remove top and right borders
    for ax in axs:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    fig.suptitle(figure_title)
    plt.tight_layout()
    plt.show()   
    
    
def box_plot_throughput_latency_turnaround(results_1, results_2, results_1_title, results_2_title, figure_title):
    """
    def box_plot_throughput_latency_turnaround(results_1, results_2, results_1_title, results_2_title, figure_title):
    Plots the median latency, mean latency, and turnaround time by throughput for two sets of results using box plots.

    Args:
        results_1 (DataFrame): A DataFrame containing the first set of results. It should have columns 'Batch Size', 'Median Latency', 'Mean Latency', and 'Time Taken'.
        results_2 (DataFrame): A DataFrame containing the second set of results. It should have columns 'Batch Size', 'Median Latency', 'Mean Latency', and 'Time Taken'.
        results_1_title (str): The title to use for the first set of results in the legend.
        results_2_title (str): The title to use for the second set of results in the legend.
        figure_title (str): The title to use for the entire figure.

    Returns:
        None
    """
    fig, axs = plt.subplots(1, 3, figsize=(10, 5))
    axs[0].boxplot([results_1['Median Latency'], results_2['Median Latency']], labels=[results_1_title, results_2_title])
    axs[0].set_title('Median Latency by Throughput')
    axs[0].set_ylabel('Latency (s)')
    axs[0].set_ylim(0, max(results_1['Median Latency'].max(), results_2['Median Latency'].max())+1)

    axs[1].boxplot([results_1['Mean Latency'], results_2['Mean Latency']], labels=[results_1_title, results_2_title])
    axs[1].set_title('Mean Latency by Throughput')
    axs[1].set_ylabel('Latency (s)')
    axs[1].set_ylim(0, max(results_1['Mean Latency'].max(), results_2['Mean Latency'].max())+1)

    
    axs[2].boxplot([results_1['Time Taken'], results_2['Time Taken']], labels=[results_1_title, results_2_title])
    axs[2].set_title('Result turnaround by Throughput')
    axs[2].set_ylabel('Turnaround (s)')
    axs[2].set_ylim(0, max(results_1['Time Taken'].max(), results_2['Time Taken'].max())+1)

    fig.suptitle(figure_title)
    plt.tight_layout()
    plt.show()