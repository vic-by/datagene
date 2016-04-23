__author__ = 'yuriybodnar'


import random
import logging
import string

class Mixer:
    def __init__(self):
        self.columns = []
        self.delimiter = ','

    def add_column(self, source_list,name=None):
        if name is not None:
            for i in range(len(source_list)):
                source_list[i]='"'+name+'"'+':'+'"'+source_list[i]+'"'
        self.columns.append(source_list)

    def set_delimiter(self, delimiter):
        self.delimiter = delimiter

    def mix(self, number_of_records=1000, with_incremental_id=False):
        result = []
        for id in range(number_of_records):
            if id % 100000 == 0:
                logging.warning("%s generated" % id)
            line = self.delimiter.join(random.choice(list) for list in self.columns)
            result.append(line)
        return result

    def json(self, number_of_records=30):
        result = []
        self.delimiter = ','
        for id in range(number_of_records):
            line = self.delimiter.join(random.choice(list) for list in self.columns)
            line = '{'+line+'}'+'\n'
            result.append(line)
        return result


def get_from_list(path, limit=None):
    if limit is not None and limit <= 0:
        raise Exception("Limit cannot be less or equal zero")

    with open(path, 'r') as raw:
        if limit is None:
            return [item.rstrip('\n') for item in  raw.readlines()]
        else:
            i = 0
            result = []
            with open(path, 'r') as raw:
                while i < limit:
                    i = i + 1
                    result.append(raw.readline().rstrip())
            return result


def flush_to_local_file(result_, file):
    global result
    file_ = open(file, mode="w")
    file_.writelines(result_)
    file_.close()
    result = []

def shuffled_ints(min=0, max=20):
    _list = range(min, max)
    random.shuffle(_list)
    return [str(item) for item in _list]

def shuffled_decs(min=0.1, max=100.2):
    _list = range(min, max)
    random.shuffle(_list)
    return [str(item) for item in _list]

def alphabet(shuffled=False):
    pass
