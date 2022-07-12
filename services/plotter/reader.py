import base64

"""
input:
X,Y
1,2
2,4
3,8
4,16
"""

def decode(encoded_data):
    """Decodes"""
    return base64.b64decode(encoded_data).decode('utf-8')


if __name__ == '__main__':
    b64_data = "WCxZCjEsMgoyLDQKMyw4CjQsMTY="

    print(decode(b64_data))
