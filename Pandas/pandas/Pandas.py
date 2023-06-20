import pandas as pd
import numpy as np

# 1. 创建序列s1，值为11-15之间的5个整数，标签为字母a、b、c、d、e。
s1 = pd.Series(np.arange(11,16),index=['a','b','c','d','e'])
print(s1)
# 2. 使用字典d1创建序列s2，d1={'浙江':'杭州','江苏':'苏州','山东':'济南','河南':'郑州','陕西':'西安'}。
d1 = {'浙江':'杭州','江苏':'苏州','山东':'济南','河南':'郑州','陕西':'西安'}
s2 = pd.Series(d1)
print(s2)
# 3. 在序列s1中执行下列操作：
# 增加元素，值为16，标签为“f”。
s1['f'] = 16
print(s1)
# 分别使用索引和标签获取值为“13”的记录。
print(s1.iloc[2],s1['c'])
# 分别使用索引和标签获取值为“12、13、14”的三条记录。
print(s1[1:4],s1['b':'d'])
# 4. 在序列s2中执行下列操作：
# 将标签为“江苏”的元素值更改为“南京”。
s2['江苏'] = '南京'
print(s2)
# 显示前5条记录。
print(s2[:5])
print(s2.head(5))
# 显示后两条记录。
print(s2.tail(2))
# 分别获得s2的标签和值。
print(s2.index,s2.values) # s2,keys()

# -------------------------------
print("-"*100)
# 创建以下数据框，值为使用NumPy随机数生成的30-100之间的10×3的数组，随机数种子为0，
# 行标签可以使用以下语句生成：
# index=map(lambda x:'A'+f'{x:03}',range(1,11))
# map()将lambda函数作用到range函数生成数据的每一个元素上，形成了A开头的顺序号。
np.random.seed(0)
data = np.random.randint(30,101,30).reshape(10,3)
index = map(lambda x: 'A'+f"{x:03d}",range(1,11))
df1 = pd.DataFrame(data,index,columns=["语文","数学","英语"])
print(df1)
# 查看“数学”列的数据类型。
print(df1['数学'].dtype)
# 使用loc方法查看行标签为A005~A008之间的数据。
print(df1.loc['A005':'A008'])
# 不使用loc或iloc查看所有的语文和英语成绩。
print(df1[['语文','英语']])
# 使用iloc方法查看行标签为A006~A008之间的语文、英语成绩。
print(df1.iloc[5:8,[0,2]])
print(df1.loc["A006":"A008",["语文","英语"]])
# 查看A005的数学成绩
print(df1.loc['A005']['数学'])
# 使用query方法查找三门课成绩均不及格的记录。
print(df1.query("语文<60 & 数学<60 & 英语<60"))
# 不使用query方法查找语文优秀（>=90）的记录。
print(df1[df1['语文']>=90])
# 使用isin方法查找英语分数正好为10的倍数（可以用range(30,101,10)表示）的记录。
print(df1[df1['英语'].isin(range(10,101,10))])
# 查看数据框一共有多少个数据项。
print(df1.size)
# 增加两列：总分和平均分（需要两条语句）。
# df1 = pd.concat([df1,pd.DataFrame([],columns=['总分','平均分'])])
df1['总分'] = df1.sum(axis=1)
df1['平均分'] = df1.mean(axis=1)
print(df1)
# 删除平均分这一列。
df1.drop(['平均分'],axis=1,inplace=True)
print(df1)
# 删除行标签为A005和A010的行。
df1.drop(['A005','A010'],inplace=True)
print(df1)
# ---------------------
print("-"*100)

# 1. 创建数据框df1，值为[1,50]之间3×4的随机整数，行标签为a、b、c，列标签为'Jan'、'Feb'、'Mar'、4月。
data = np.random.randint(1,51,12).reshape(3,4)
index = ['a','b','c']
columns = ['Jan','Feb','Mar','4月']
df1 = pd.DataFrame(data,index,columns)
print(df1)
# 2. 将df1的行标签更改为a、c、E。
df1.index = ['a','c','E'] # list['acE']
print(df1)
# 3. 将“4月”的列名更改为“Apr”、将行标签“E”更改为“e”。
df1.rename(columns={'4月':'Apr'},inplace=True)
df1.rename(index={'E':'e'},inplace=True)
print(df1)
# 4. 使用重建索引找出行标签为['a','b','c','d']的数据。
print(df1.reindex(['a','b','c','d']))

# ---------------

# 创建数据框df2，值为使用NumPy随机数生成的30-100之间的10×3的数组，随机数种子为0，
# 1. 行标签可以使用以下语句生成：
np.random.seed(0)
data = np.random.randint(30,101,30).reshape(10,3)
index = map(lambda x:f"A{x:03d}",range(1,11))
df2 = pd.DataFrame(data,index,columns=['语文','数学','英语'])
print(df2)
# 5.定义一个成绩等级映射函数f：[90,+)为A，[80,89)为B，[70,79)为C，[60,69)为D，(-,60]为E。
# 然后将该函数作用到“语文”，结果如下：
def f(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'E'
print(df2['语文'].apply(f))

# 6. 计算每门课中每个成绩相对该课程平均分的差值，结果如下：
print(df2.apply(lambda col:col-col.mean(),axis=0))

# 7. 利用第（5）题中定义的函数f，计算每个成绩的成绩等级，结果如下。
print(df2.applymap(f))
# 8. 将df2原地排序，按数学成绩降序排序，数学成绩相等时再按英语成绩的降序排序。
df2.sort_values(['数学','英语'],ascending=[False,False],inplace=True)
print(df2)
# 9. 将df2按照索引的升序排序。
print(df2.sort_index(ascending=True,inplace=True))
# 10. 增加“总分”列，每列为每个学生的三门课分数之和。增加“排名”列，
# 按照总分成绩从高到低排序给出排名，总分相等时排名相同， 
# 取最好排名值（排名靠前）。结果如下。
df2['总分'] = df2.sum(axis=1)
df2['排名'] = df2['总分'].rank(ascending=False,method='max') #降序
print(df2)
df2.drop(['总分','排名'],axis=1,inplace=True)
# 11. 计算三门课的各自的总分。如下所示。
print(df2.sum(axis=0))
# 12 计算三门课的各自的平均分。如下所示。
print(df2.mean(axis=0))
# 13. 计算语文课程不及格的人数。提示：先判断语文每个值是否小于60，然后使用sum方法汇总。
print(np.sum(df2['语文']<60))
# 14. 求英语成绩最高的5个值和最低的3个值。
print(df2['英语'].nlargest(5))  #print(df2['英语'].sort_values(ascending=False).head(5))
print(df2['英语'].nsmallest(3)) #print(df2['英语'].sort_values(ascending=True).head(3))
# 15. 求语文成绩最高的3条记录以及数学最低的5条记录。
print(df2.nlargest(3,['语文'])) #print(df2.sort_values(['语文'],ascending=False).head(3))
print(df2.nsmallest(5,['数学'])) #print(df2.sort_values(['数学'],ascending=True).head(5))
# 16. 查看三门课的统计信息，如下图所示。
print(df2.iloc[:,:3].describe())