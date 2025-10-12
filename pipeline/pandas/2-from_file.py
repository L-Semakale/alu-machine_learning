import pandas as pd

def from_file(filename, delimiter):
    """
    Loads data from a file as a pd.DataFrame

    Args:
    filename (str): the file to load from
    delimiter (str): the column separator

    Returns:
    pd.DataFrame: the loaded DataFrame
    """
    return pd.read_csv(filename, delimiter=delimiter)import pandas as pd

def from_file(filename, delimiter):
    """
    Loads data from a file as a pandas DataFrame
    
    Args:
        filename (str): The file to load from
        delimiter (str): The column separator
        
    Returns:
        pandas.DataFrame: The loaded DataFrame
    """
    # Load the file into a DataFrame using pandas.read_csv()
    # Note: read_csv() works for any delimiter, not just commas
    df = pd.DataFrame(pd.read_csv(filename, delimiter=delimiter))
    
    return df
