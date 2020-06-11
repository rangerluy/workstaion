# 各中获取表与处理表的函数
import pandas as pd
# 获取整个表的数据
def get_data_excel(excel_name,column_name):
    df = pd.read_excel(excel_name,keep_default_na=False)
    return [i for i in df[column_name]]
# 9999 住院时长
def data_9999_1(zd):
    return [zd[i] for i in range(len())]


