"""TODO: Read account data"""


def __read_key(filename):
    file = open(filename, 'r')
    key = file.readline()
    file.close()
    return key
