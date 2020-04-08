"""
Python push up functions
"""
def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string.
    If the string length is less than 3, the front is whatever is there.
    Return a new string which is 3 copies of the front.
    :param str:
    :return str:
    """
    result = ""
    if len(str) < 3:
        result = str*3
        return result
    result = str[:3]*3
    return result
