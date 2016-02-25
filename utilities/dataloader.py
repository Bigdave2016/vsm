__author__ = 'uyaseen'


def load_data(fname):
    f = open(fname, 'r')
    doc = f.read()
    f.close()
    return doc