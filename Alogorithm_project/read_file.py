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
    # # print(df.index)
    # for i in df.index:
    # 	ti = pd.to_datetime(str(i))
    # 	d = ti.strftime('%Y-%m-%d')
    df.index.rename("datetime")
    print(df)


if __name__ == '__main__':
	read_file()
