import argparse

import pandas as pd

def main(filename):
    print(' -------Cleaning data------- ')
    print('...')

    df = _read_data(filename)

    df = _clean_lists(df)

    return df

def _read_data(filename):
    
    print(f'Reading file {filename} ...')

    return pd.read_csv(filename)


def _clean_lists(df):
    print('Cleaning list...')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument ('filename',
                         help='The path to the dirty data',
                         type=str)
    args = parser.parse_args()
    df = main(args.filename)

    print('Transform is done!')