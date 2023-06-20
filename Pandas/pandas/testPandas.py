import pandas as pd
import numpy as np
# items = [1,2,3,4]
items = np.array(['a','b','c','d'])
# dict = {"name":"ylh","age":18}
s = pd.Series(items)
print(s)
s[0]='r'
print(s[::-1])
print(s[2:3])

data = [1,2,3]
df = pd.DataFrame(data)
print(df)

data = [['Axel',32], ['Alice', 26], ['Alex', 45]]
df = pd.DataFrame(data,columns=["Name","age"])
print(df)
print(df["Name"])
print(df['age'])

# 增加一列
add = pd.DataFrame([1,2,3],columns=["num"])
df["num"] = add["num"]
print(df)

# 删除列
del df["num"]
print(df)

# 选择某一行
print(df.loc[2])  # index名字
print(df.iloc[0])

# 添加一行
user = pd.DataFrame([['Vivian',33]], columns= ['Name','age'])
# df = df.append(user)  As of pandas 2.0, append (previously deprecated) was removed.
df = pd.concat([df,pd.DataFrame([["Ylh",20]],columns=["Name","age"],index=[3])]) # Series或 DataFrame序列
df.loc[len(df)] = ["Lxy",18]
print(df)

# 删除行
df.drop([0,1,2],inplace=True)
print(df)

# 使用字典创建DataFrame
d = {'one':[1,2,3], 'two':[4,5,6], 'three':[7,8,9] } # 默认作为columns值
df = pd.DataFrame(d,index=["frist","second","third"]) 
print(df)

# 从array创建DataFrame
arr = np.arange(20).reshape(4,5)
d2 = pd.DataFrame(arr,columns=["One","Two","Three","Four","Five"],index=["A","B","C","D"])
print(d2)

# 从DataFrame创建DataFrame
d3 = d2[["One","Two"]].copy()
print(d3)

d3.to_excel("pandas_to_excel.xlsx")

d4 = pd.read_excel("pandas_to_excel.xlsx")
print(d4)