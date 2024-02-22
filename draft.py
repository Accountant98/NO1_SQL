import streamlit as st
import pandas as pd
import base64
import xlwings
# Sample DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)

# Streamlit ap


import pandas as pd

# Tạo một DataFrame ví dụ
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
# Đặt lại chỉ số cột về từ 0
df.reset_index(drop=True, inplace=True)

# In ra DataFrame sau khi đã đặt lại chỉ số cột
print(df)
