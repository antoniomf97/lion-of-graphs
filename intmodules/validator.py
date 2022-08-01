

def check_numeric_values(data):
    """Checks if given data is of type float"""
    try:
        for col in data.columns:
            data[col] = data[col].astype(float)
    except ValueError:
        print("Data is invalid for processing: found string data instead of numeric.")
        exit()


def check_null_values(data):
    """Checks if there are any null values and how many"""
    data_nulls = data.isnull()
    if data_nulls.any().any():
        print("Data is invalid for processing: founded {} NaN values.".format(data_nulls.sum().sum()))
        exit()
        return False
    else:
        return True


def check_index_duplicates(data):
    """Check if data index has duplicates"""
    index = data.index.values
    if len(index) == len(set(index)):
        return True
    else:
        print("Data is invalid for processing: duplicated abscissa.")
        exit()
        return False


def validate_data(data):
    """Validates input data for general plot"""
    check_null_values(data)
    check_numeric_values(data)
    check_index_duplicates(data)


