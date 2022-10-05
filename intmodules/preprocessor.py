from intmodules.exceptions import DuplicatedEntryError, NanValueFoundError


def validate_data(dataframe):
    """Validates input data"""
    data_nulls = dataframe.isnull()
    if data_nulls.any().any():
        raise NanValueFoundError

    for col in dataframe.columns:
        dataframe[col] = dataframe[col].astype(float)

    index = dataframe.index.values
    if not len(index) == len(set(index)):
        raise DuplicatedEntryError

    return dataframe
