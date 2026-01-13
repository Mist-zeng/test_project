import pandas as pd
from datetime import datetime
import numpy as np
input_emp_path = 'D:\_734919\員工名單1027TO 福委.xlsx'
input_bonus_path = 'D:\_734919\各單位福委.xlsx'
output_path = 'D:\_734919\_test_data.xlsx'
print(input_emp_path)
print(input_bonus_path)

df_emp = pd.read_excel(input_emp_path, dtype='str', sheet_name='1027員工名單')
df_bonus = pd.read_excel(input_bonus_path, dtype='str')
print(df_emp.dtypes)
print(df_bonus.dtypes)

#資料清洗
df_emp = df_emp.astype(str).replace(r'^\s+|\s+$', '', regex=True)
df_emp.replace(['', 'nan'], np.nan, inplace=True)
df_bonus = df_bonus.astype(str).replace(r'^\s+|\s+$', '', regex=True)
df_bonus.replace(['', 'nan'], np.nan, inplace=True)
df_emp = df_emp[df_emp['職等職稱'] != '顧問']
df_merge = df_emp.merge(df_bonus, on=['工作地', '部門', '課別'], how='left')
print(df_merge.dtypes)

df_merge.to_excel(output_path, index=False)

#日期合法性判斷
def date_check(prompt = '請輸入三節日期(YYYYMMDD)：'):
    while True:
        bonus_str = input(prompt).strip()
        try:
            bonus_date = datetime.strptime(bonus_str, '%Y%m%d')
            print(f'日期檢核正確，輸入日期為{bonus_str}')
            return bonus_date
        except ValueError:
            print(f'日期檢核錯誤，請重新輸入')

#年資判斷
def workday_check():
    df_emp['入職日'] = df_emp['']


#條件判斷
# 三節獎金年資須滿三個月，且不補發，均以節日日期為準
# 51統一1000
# 端午跟中秋大於等於三個月1000，大於等於一年以上2000
# 聖誕禮金手動輸入預算金額/領取人數向下取整到百位
