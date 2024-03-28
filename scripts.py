import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def cleaning(data, missing = None, drop_threshold = 0.2):
    '''
    Drops columns with a higher proportion of missing values than the drop threshold and imputes remaining missing values.
    Numerics are mean-imputed and everything else is mode-imputed.
    '''
    data.replace(-99999, np.nan, inplace = True)

    original_shape = data.shape
    n_missing = data.isna().sum().sum()
    _ = data.isna().sum() != 0
    col_missing = data.isna().sum()[_].index
    n_col_missing = (data.isna().sum() != 0).sum()

    n_drop_threshold = int(len(data) * drop_threshold)
    imputed_cols = []
    for column in data.columns:
        if data[column].isna().sum() == 0:
            continue
        if data[column].isna().sum() > n_drop_threshold:
            data.drop(column, axis = 1, inplace = True)
            continue
        imputed_cols.append(column)
        if is_numeric_dtype(data[column]) == False:
            data[column].fillna(data[column].mode(), inplace = True)
            continue
        _ = data[column].dropna()
        data[column].fillna(_.mean(), inplace = True)
    print(f'Your original data was missing {n_missing} values across {n_col_missing} columns. These columns are: {col_missing}')
    print(f'As a result of cleaning your data\'s shape has changed from: {original_shape} to {data.shape}.')
    print(f'Columns: {imputed_cols} have undergone imputation.')
    return data

def splitting(data, target, test = 0.2, preserve = None):
    '''
    Splits data with a minimum test-set size, ensuring the test data and train data have no commonality in column `preserve`.
    '''
    if preserve == None:
        return 'Please enter which column you would like to preserve, otherwise use scikit-learn\'s train_test_split'
    target_test_n = int(len(data) * 0.2)
    test_n = 0

    test_groups = []
    grouped_data_size = data.groupby(preserve).size().sort_values()
    for group in grouped_data_size.index:
        if test_n < target_test_n:
            test_n += grouped_data_size[group]
            test_groups.append(group)
            continue
        break
    X_train = data[~data[preserve].isin(test_groups)].drop(target, axis = 1)
    X_test = data[data[preserve].isin(test_groups)].drop(target, axis = 1)
    y_train = data[~data[preserve].isin(test_groups)][target]
    y_test = data[data[preserve].isin(test_groups)][target]
    print(f'Columns {preserve} contained {len(data[preserve].unique())} unique values. After splitting, {len(X_train[preserve].unique())} are in the training data and {len(X_test[preserve].unique())} are in the testing data.')
    print(f'The training data has a length of {len(X_train)} and the testing data has a length of {len(X_test)}.')
    return X_train, X_test, y_train, y_test