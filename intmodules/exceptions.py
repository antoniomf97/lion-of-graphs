class InvalidJsonSchemaError(Exception):
    """Specifies validation error on JSON schema validation"""
    def __init__(self):
        super().__init__(self)


class NanValueFoundError(Exception):
    """Specifies found NaN value(s) error on data validation"""
    def __init__(self):
        super().__init__(self)


class DuplicatedEntryError(Exception):
    """Specifies duplicated entry error on data validation"""
    def __init__(self):
        super().__init__(self)

