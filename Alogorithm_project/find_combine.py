import pandas as pd
import warnings
from itertools import combinations
import time


warnings.simplefilter(action="ignore", category=FutureWarning)


def read_file():
    """
    :return:
    dataframe : input from file
    """
    df = pd.ExcelFile("./data/test.xls")
    df = df.parse("Sheet1").fillna("0")
    df = df.convert_objects(convert_numeric=True)
    return df


# Count value in each row
def count_value_row():
    df = read_file()
    drow = df.sum(axis=1)
    print(drow.count())


# Count value in each column
def count_value_column():
    df = read_file()
    dcolumn = df.sum(axis=1)
    print(dcolumn)


def processing_input():
    """
    :return:
    dataframe
    """
    df = read_file()
    # df = df.convert_objects(convert_numeric=True)
    # Count Sum of value in each column
    ds = df.sum(axis=0)
    va_dict = ds.to_dict()
    # print(va_dict)
    return va_dict


# def sortting():
#     va_dict = processing_input()
#     sorted_x = sorted(va_dict.items(), key=operator.itemgetter(1), reverse=True)
#     return va_dict


def find_combinations():
    start_time = time.time()
    va_dict = processing_input()
    keys = va_dict.keys()
    for i in combinations(keys, 4):
        print(str(i), (str(va_dict[i[0]] + va_dict[i[1]] + va_dict[i[1]])))
    print(time.time() - start_time)


def convert_time():

    return


if __name__ == '__main__':
    read_file()
    processing_input()
    find_combinations()

