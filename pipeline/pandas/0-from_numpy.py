import pandas as pd
import numpy as np
import string

def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy array.
    
    Args:
        array (numpy.ndarray): The input numpy array
        
    Returns:
        pandas.DataFrame: A DataFrame with alphabetically labeled, capitalized columns
    """
    # Get the number of columns in the array
    num_cols = array.shape[1]
    
    # Generate alphabetical column names (A, B, C, ...) based on the number of columns
    column_names = [string.ascii_uppercase[i] for i in range(num_cols)]
    
    # Create the DataFrame with the array and column names
    df = pd.DataFrame(array, columns=column_names)
    
    return df
