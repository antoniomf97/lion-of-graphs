class NanValueFoundError(Exception):
    """Specifies found NaN value(s) error on data validation"""
    def __init__(self):
        super().__init__(self)


class DuplicatedEntryError(Exception):
    """Specifies duplicated entry error on data validation"""
    def __init__(self):
        super().__init__(self)


class InvalidRequestError(Exception):
    """Specifies duplicated entry error on data validation"""
    def __init__(self):
        super().__init__(self)
