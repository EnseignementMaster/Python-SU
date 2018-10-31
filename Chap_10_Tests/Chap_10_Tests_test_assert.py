

def coding(message, key, isCoding):
    """
    code the given message with the given key.
    If the boolean is_coding is true we code the message. Otherwise we decode it.
    return the new message (coded or decoded)
    """
    assert type(message) is str, \
        "message is not a string: {}".format(message)
    assert type(key) is int, \
        "message is not a string: {}".format(message)
    assert (type(isCoding) is str) \
           and (isCoding == "True" or isCoding == "False"), \
        "isCoding should be equal to 'True' or 'False'"


coding('titi', 3, 'True')
