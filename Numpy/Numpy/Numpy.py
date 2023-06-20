from hashlib import sha384
import numpy as np

M = [[1,3],[2,4]]

def work():
    arr1 = np.array([1,2,3,4,5,6],dtype=int)
    print(f"转变为list: {arr1.tolist()}")
    print(f"数组的维数: {arr1.ndim}")
    print(f"数组的元素个数: {arr1.size}")
    print(f"数组的元素类型: {arr1.dtype}")
    print(f"数组的形状: {arr1.shape}")


# ------------------------
# 1. 建立列表ls=[1,2,3,10], 基于ls建立数组a1，元素类型为int；建立元组tp=(2,4,6,9,4)，基于tp建立数组a2，元素类型为float。
ls = [1,2,3,10]
a1 = np.array(ls,dtype=int)
tp = (2,4,6,9,4)
a2 = np.array(tp,dtype=float)
print(a1,a2)
# 2. 建立4×4的全0数组a3、全1数组a4、单位数组a5和对角线为[10,20,30,40]的数组a6。 
a3 = np.zeros([4,4])
a4 = np.ones([4,4])
a5 = np.eye(4,4)
a6 = np.diag([10,20,30,40])
print(a3,a4,a5,a6)
# 3. 建立4×6的随机整数数组a7，数组元素在[0,50]之间。
a7 = np.random.randint(0,51,size=[4,6])
print(a7)
# 4. 使用arange()函数和reshape()函数创建4×6的数组a8，数组元素为0-23之间的整数。
a8 = np.arange(0,24).reshape(4,6)
print(a8)
# 5. 建立[0,100]之间的等差数组，其中a9数组包含终点100在内一共有12个元素，a10数组不包含终点100在内一共有12个元素。
a9 = np.linspace(0,100,12,endpoint=True)
a10 = np.linspace(0,100,12,endpoint=False)
print(a9)
print(a10)
# 6.建立1-10000之间的等比数组a11，包括终点10000在内一共有6个元素。
a11 = np.logspace(1,4,6,endpoint=True)
print(a11)
# 7. 分别查看数组a2和a7的维度、形状、元素总数、每个元素的大小。
print(f"a2的维度: {a2.ndim} a7的维度: {a7.ndim}")
print(f"a2的形状: {a2.shape} a7的形状: {a7.shape}")
print(a2.size,a7.size)
print(a2.itemsize,a7.itemsize)  
# 8.修改a8的形状为8×3。
a8.shape=8,3
print(a8)
# 9.
print(a7[[1,-1]])
print(a7[:,[2,3]])
# 11. 判断a8中元素是否是奇数，给出二维布尔数组，给出具体的奇数值，然后将所有奇数值统一用100替换。
print(a8)
print(a8[a8%2==1])
a8[a8%2==1]=100
print(a8)
# 12. 找出a7中[10,20]之间的元素。
print(a7[(a7>=10) & (a7<=20)])
# 13. 用np.where()函数实现将a7中[10,20]之间的元素用0替换，其它元素用1替换，输出替换后的数组。原数组a7不要求改变
print("-------------------")
t = np.where((a7>=10) & (a7<=20),0,1)
print(t)
# 14. 使用append()将a4追加到a3后面，数组形状为8×4，仅返回结果，数组a3保持不变。
print(np.append(a3,a4).reshape(8,4))
# 15. 将数组a3插入到数组a4的第0行，仅返回结果，数组a4保持不变
print(np.insert(a4,0,a3,axis=0))
# 16. 将数组a3插入到数组a4的第1列，仅返回结果，数组a4保持不变。
print(np.insert(a4,1,a3,axis=1))
# 17. 使用np.delete()在数组a7中执行下列操作：分别删除第0个和最后一个位置元素、删除第0行和最后一行、删除第0列和最后一列。上述操作只需返回删除后的结果，均不要改变a7中的元素。
print(np.delete(a7,0))
print(np.delete(a7,-1))
print(np.delete(a7,0,axis=0))
print(np.delete(a7,-1,axis=0))
print(np.delete(a7,0,axis=1))
print(np.delete(a7,-1,axis=1))
# 18. 分别使用hstack()、column_stack()、concatenate()实现数组a3和a4的水平合并。
print(np.hstack((a3,a4)))
print(np.column_stack((a3,a4)))
print(np.concatenate((a3,a4),axis=1))
# 19. 分别使用vstack()、row_stack()、concatenate()实现数组a3和a4的垂直合并
print(np.vstack((a3,a4)))
print(np.row_stack((a3,a4)))
print(np.concatenate((a3,a4),axis=0))
# 20. 分别使用hsplit()和split()函数实现数组a8（形状为3×8）水平分割为3个数组，第1个数组为前2列，第2个数组中第3、4、5列，剩余为第3个数组
a8.shape=3,8
print(np.hsplit(a8,[2,5]))
print(np.split(a8,[2,5],axis=1))
# 21. 分别使用vsplit()和split()函数实现数组a7（形状为6×6）水平分割为3个数组，第1个数组为第1行，第2个数组为2、3行，第3个数组为剩余列。
a7 = np.append(a7,a7[[-2,-1]],axis=0).reshape(6,6)
print(np.vsplit(a7,[1,3]))

# ----------------------------
# 1.
m1 = np.mat([[1, 2, 3], [4, 5, 6]])
m2 = np.matrix([[0,2,4],[6,8,10]])
m3 = np.bmat([[m1,m2],[m2,m1]])
print(m3)
# 2. m1*2    m1+m2        m2/2             m1*m2.T   np.multiply(m1,m2)
print(m1*2)
print(m1+m2)
print(np.multiply(m1,m2))
# 3. 使用np.random模块创建1~10之间的随机数组a1，形状为3×4。创建数组a2，语句为a2=a1*10。然后执行下列数组运算，查看结果，确认结果的正确性。
a1 = np.random.randint(1,11,12).reshape(3,4)
a2 = a1*10
print(a1)
print(a2)
# 4.
#分别写出下列条件表达式：
#判断a1的每个元素是否大于5，返回布尔数组；
#判断a1的每个元素是否等于6，返回布尔数组；
#判断a1中所有元素是否都大于1，返回一个布尔值；
#判断a1中是否有元素大于8，返回一个布尔值。
print(a1>5)
print(a1==6)
print(np.all(a1>1))
print(np.any(a1>8))
# 3. 
a3 = np.random.randint(1,51,24).reshape(4,6)
a4 = a3.copy()
print(a3)
a3.sort()
print(a3)
print(np.sort(a4,axis=0))
print(a4)
# 6. 创建包含10个元素的一维随机数组a5，元素为[10,20]之间的整数。将a5降序输出
a5 = np.random.randint(10,21,10)
print(a5)
print(-np.sort(-a5))
print(np.argsort(-a5))
# 7. 统计a5中每个元素出现的次数，用元组返回结果
print(a5)
print(np.unique(a5,return_counts=True))
# 8. 
print(np.max(a5),np.min(a5),np.sum(a5),np.mean(a5),np.std(a5))
# 9. 使用数组合并将数组a3每行数据的和，放在a3最后一列并显示。
print(a3)
print()
# print(np.append(a3,np.mat(np.sum(a3,axis=1)).T,axis=1))
print(np.hstack((a3,a3.sum(axis=1).reshape(4,1))))
print(np.column_stack((a3,a3.sum(axis=1).reshape(4,1))))
print(np.concatenate((a3,a3.sum(axis=1).reshape(4,1)),axis=1))
# 10. 有三颗骰子，每次一起抛出，现在用随机函数模拟抛掷1000次。
# 这1000次中有多少次抛出“666”？有多少次出现抛出的三个骰子点数一样？编写程序，输出结果如下：
def lowFunction():
    cnt = 0
    sum = 0
    for i in range(1000):
        s1 = np.random.randint(1,7)
        s2 = np.random.randint(1,7)
        s3 = np.random.randint(1,7)
        if s1 == s2 == s3:
            if s1 == 6:
                cnt+=1
            sum+=1
    print(f"有{cnt}次抛出666，有{sum}次点数相同")
def NumpyWriteToFile(file,arr):
    np.save(file,arr)
    np.savetxt("".join([file,"_txt.txt"]),arr)
def highFunction():
    np.random.seed(7)
    nums = 1000
    choice = np.random.randint(1,7,[nums,3])
    choice = np.hstack((choice,choice.sum(axis=1).reshape(nums,1)))
    NumpyWriteToFile("throw",choice)
    # 6 6 6
    print(np.sum(choice[:,-1]==18))
    # x x x
    situation = (choice[:,0]==choice[:,1]) & (choice[:,1]==choice[:,2])
    print(np.sum(situation))
    # output
    print(choice[situation][:,[0,1,2]])


# highFunction()

a1 = np.arange(9).reshape(3,3)
a2 = np.arange(9,18).reshape(3,3)
print(a1)
print(a2)
print(np.hstack((a1,a2))) # horizon
print(np.vstack((a1,a2))) # vertical
print(np.concatenate((a1,a2),axis=1))


# load from .npyfile
arr = np.load("throw.npy")
arr2 = np.loadtxt("throw_txt.txt")
print(arr)
print(arr2)