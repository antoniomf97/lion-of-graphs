

def check_duplicates(data):
    """Check if data has duplicates"""
    return len(data) != len(set(data))


def validate_data(data):
    """Validates input data for general plot"""
    if check_duplicates(data.index.values):
        return True
    else:
        print("Data is invalid for plotting: duplicated abscissa")
        return False
