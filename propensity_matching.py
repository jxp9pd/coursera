"""Treatment effect of NSW on employment impact"""
import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tableone import TableOne
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 100)

LOCAL_PATH = "C:/Users/jopentak/Development/coursera/data/"
#%%Read in observational data

lalonde = pd.read_csv(LOCAL_PATH + 'lalonde.csv')
lalonde['Outcome'] = lalonde['re78'] - lalonde['re74']
treatment = lalonde[lalonde.treat == 1]
control = lalonde[lalonde.treat == 0]
covariates = ['age', 'educ', 'black', 'hispan', 'married', 'nodegree', 're74', 're75']
#%%Pre treatment distributions.

def hist_plot(c, t, title):
    """Plots the distributions for control and treatment"""
    n_bins=10
    plt.subplot(1, 2, 1)
    plt.hist(c, bins=n_bins, edgecolor='black', linewidth=1)
    plt.title('Treatment ' + title)
    plt.subplot(1, 2, 2)
    plt.hist(t, bins=n_bins, edgecolor='black', linewidth=1)
    plt.title('Control ' + title)
    plt.show()
hist_plot(treatment.re74, control.re74, '1974 income')
#%%