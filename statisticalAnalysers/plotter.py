import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, plot_results_path, verbose=True):
        # type: -> None:
        if not os.path.exists(plot_results_path):
            os.mkdir(plot_results_path)
        self.path = plot_results_path
        self.verbose = verbose

    def plot_info_model(self, info_model, title):
        labels = info_model.get_keys()
        df = info_model.get_dataframe()
        df.plot(x=df.columns[0], y=df.columns[1:], kind="bar",figsize=(9,8), \
            title=title)
        plt.savefig(os.path.join(self.path, title + ".jpg"))
        if self.verbose:
            plt.show()
