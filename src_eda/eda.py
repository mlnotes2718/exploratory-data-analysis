# eda.py

import pandas as pd
import numpy as np

def data_quality(df):
    """
    Assess the quality of the DataFrame
    """

    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate rows found.")
        df[df.duplicated(keep=False)].sort_values(by=list(df.columns))
        duplicates_percentage = df.duplicated().sum() / len(df) * 100
        print(f"Duplicate rows percentage: {duplicates_percentage:.2f}%")

    # Print report
    print("Data Quality Report:")
    print(f"Total rows: {len(df)}")
    print(f"Total columns: {df.shape[1]}")
    print(f"Duplicate rows: {duplicates}")
    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate rows found.")
        df[df.duplicated(keep=False)].sort_values(by=list(df.columns))
        duplicates_percentage = df.duplicated().sum() / len(df) * 100
        print(f"Duplicate rows percentage: {duplicates_percentage:.2f}%")


    # Check for data structures and types and missing values
    print(df.info())

    # Get numerical columns names and categorical columns names
    numerical_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    temporal_columns = df.select_dtypes(include=['datetime']).columns

    # Print the numerical and categorical columns
    print("Numerical columns:", numerical_columns)
    print("Categorical columns:", categorical_columns)
    print("Temporal columns:", temporal_columns)

    # Missing data columns
    missing_data = df.columns[df.isnull().any()].tolist()
    print("Columns with missing data:", missing_data)

    # anomaly analysis for numerical columns
    print(df[numerical_columns].describe())