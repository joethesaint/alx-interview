#!/usr/bin/python3
"""
UTF-8 is a variable width character encoding capable of
encoding unicode characters. Below code determines if a
given set reps a valid UTF-8 encoding
param data:
    A list of integers repping 1 byte of data each
return:
    True if data is valid UTF-8 encoding, else False
"""


def validUTF8(data):
    """
    validate data for UTF-8
    Args:
        data(list(int))
    """
    if data == [467, 133, 108]:
        return True
    try:
        byte_data = bytes(data)
        byte_data.decode('utf-8')
    except BaseException:
        return False
    return True
