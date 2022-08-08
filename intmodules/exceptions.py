class InvalidJsonFormatError(Exception):
    def __init__(self):
        super().__init__(self)


class InvalidJsonSchemaError(Exception):
    def __init__(self):
        super().__init__(self)


class NonNumericValueFoundError(Exception):
    def __init__(self):
        super().__init__(self)


class NanValueFoundError(Exception):
    def __init__(self):
        super().__init__(self)


class DuplicatedEntryError(Exception):
    def __init__(self):
        super().__init__(self)


class InvalidBase64EncodingError(Exception):
    def __init__(self):
        super().__init__(self)


class InvalidCharacterUtf8EncodingError(Exception):
    def __init__(self):
        super().__init__(self)


class StringToDataframeError(Exception):
    def __init__(self):
        super().__init__(self)

