import pandas as pd

def load_data(fname):
    '''
    Reads a csv and gives the dataframe
    '''

    df = pd.read_csv(fname)
    return df


