import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("--- 6G smart Factory Data Analysis Pipeline Initialized ---")

def load_and_summarize_dta(file_path):
  """
  Loads manufacturing sensors logs and prints shape and basic statistics.
  """
  try:
    # Load dataset once provided by Unified Mentor
    df = pd,read_csv(file_path)
    print(f"Successfully loaded data set with {df.shape[0]} rows and {df.shape[1]} columns.\n")

    #Display basic metadata
    print("--- Dataset Information---")
    print(df.info())

 # Process Health  & OEE checks
    print("\n---Basic Statistical Summary ---")
    print(df.describe())
    return df
 execpt FileNotFoundError:
 print(f"Error: Dataset not found at {file_path}. Please upload your CSV file to data/raw/folder.")
return None

if__name__=="__main__":
# Path where your dataset  will live
DATA_PATH = "../data/raw/manufacturing_data.csv"
load_and_summarize_data(DATA_PATH)
 
