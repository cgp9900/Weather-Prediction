def my_train_split(X, y, test_size=0.2):
    # Custom, simple train test split function with a default
    # test size of 0.2. Function calculates the position at which
    # train and test data will split, and then indexes accordingly.
    data_length = len(X)
    data_breakpoint = int(data_length - data_length * test_size)
    X = X.sort_values()
    X_train = X[:data_breakpoint]
    X_test = X[data_breakpoint:]
    y_train = y[:data_breakpoint]
    y_test = y[data_breakpoint:]
    return X_train, X_test, y_train, y_test
