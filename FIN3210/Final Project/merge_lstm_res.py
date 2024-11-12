import glob
import os
import numpy as np
import pandas as pd

# Help me use glob to read the files containing LSTM_result_*.csv
# and merge them into one file
# The files are in the same directory as this script
# The merged file is named LSTM_result_merged.csv

# Get the current directory
current_dir = os.getcwd()
# Get the files to be merged
files = glob.glob(current_dir + '/LSTM_result_*.csv')
# Read the files and merge them
dfs = [pd.read_csv(f) for f in files]
merged = pd.concat(dfs, ignore_index=True)
# Write the merged file
merged.to_csv('LSTM_result_merged.csv', index=False)