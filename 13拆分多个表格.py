import pandas as pd
import os

fn=input(r'请输入文件路径')
while os.path.exists(fn) is False:
    fn=input(r'文件不存在，重新输入文件路径')
df=pd.read_excel(fn)
#print(df)

col=input('请输入列名')

while col not in df:
    col = input('列不存在，重新输入列名')

df1=df.groupby(col)
for a,b in df1:
    print(a)
    print(b)
    b.to_excel(f'D:\{a}.xlsx')
