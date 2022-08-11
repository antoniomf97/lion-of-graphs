from intmodules.exceptions import DuplicatedEntryError, NanValueFoundError


def check_numeric_values(data):
    """Checks if given data is of type float"""
    for col in data.columns:
        data[col] = data[col].astype(float)


def check_null_values(data):
    """Checks if there are any null values and how many"""
    data_nulls = data.isnull()
    if data_nulls.any().any():
        raise NanValueFoundError


def check_index_duplicates(data):
    """Check if data index has duplicates"""
    index = data.index.values
    if not len(index) == len(set(index)):
        raise DuplicatedEntryError


def validate_data(data):
    """Validates input data for general plot"""
    check_null_values(data)
    check_numeric_values(data)
    check_index_duplicates(data)


