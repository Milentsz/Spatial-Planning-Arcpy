'''
实现用地用海自动统计面积和占比，可以分大类和中小类统计，每个大类实现小计，自动读取三调基数转换生成的YDYHFL字段
'''
import arcpy
import pandas as pd
import numpy as np

# 插入行函数
def addrow(df, i, df_add):
    # 指定第i行插入一行数据
    df1 = df.iloc[:i, :]
    df2 = df.iloc[i:, :]
    df_new = pd.concat([df1, df_add, df2], ignore_index=True)
    return df_new

# 获得属性列表
def GetFieldValueList(inTable, inField):
    value_list = []
    rows = arcpy.da.SearchCursor(inTable, inField)
    for row in rows:
        value_list.append(row[0])
    del row
    del rows
    return value_list

table = '输入的要素'

s1, s1n = GetFieldValueList(
    table, 'YDYHFLDM'), GetFieldValueList(table, 'YDYHFLMC')
s2 = GetFieldValueList(table, 'Shape_Area')

df = pd.DataFrame({'一级代码': None, '一级名称': None, '用地代码': s1, '用地名称': s1n, '面积': s2})
df['一级代码'] = df['用地代码'].map(lambda x: str(x)[:2])
df['一级名称'] = df['一级代码'].apply(lambda x : YDYHDL[x])

dfgroup = df.groupby(['一级代码', '一级名称', '用地代码', '用地名称']).sum()/10000
dfnew = dfgroup.reset_index(drop=False)

df_repeatbool = dfnew.duplicated('用地名称', keep=False)
mj_sum = dfnew['面积'].sum()
dfnew['占比'] = (dfnew['面积'] / mj_sum) * 100
dfnew.loc['合计'] = dfnew[['面积', '占比']].sum(axis=0)  # 增加汇总行
df1 = dfnew.groupby(['一级代码', '一级名称']).sum().reset_index(drop=False)  # 一级类汇总
dfnew['一级代码'] = dfnew['一级名称'] = np.nan

n = -1
m = -1
for i in df_DMREP:
    n += 1
    if i:
        continue
    else:
        m += 1
        dfnew = addrow(dfnew, n+m, df1.iloc[m:m+1,])

dfnew.iloc[-1, 1] = '总计'
dfnew.iloc[-1, 0] = '  '
dfnew = dfnew.round({'面积': 2, '占比': 2})
dfnew=dfnew.fillna('') #NaN空值填充
resultPath = r'D:\表格.xlsx'
dfnew.to_excel(resultPath, sheet_name="汇总", index=False)
