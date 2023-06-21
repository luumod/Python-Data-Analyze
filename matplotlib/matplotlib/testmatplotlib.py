from cProfile import label
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False
plt.rcParams['font.size']=13


plt.figure(figsize=[6,4])
# y=sin(x)+x^2, 0<=x<=2pi
x = np.linspace(0,2*np.pi,256)
y = np.sin(x) + x**2
plt.plot(x,y)
# plt.show()

# y=x^3+2x^2+1, -2<=x<=2
x = np.linspace(-2,2)
y = x**3 + 2*x**2 + 1
plt.plot(x,y)
# plt.show()

# 在同一副图中分别绘制正弦函数曲线、余弦函数、和正弦值+余弦值曲线。要求：
#（1）x轴的取值范围为[-2pi, 2pi]，y轴取值范围为[-2, 2]。
plt.xlim(-2*np.pi,2*np.pi)
plt.ylim(-2,2)
#（2）正弦曲线为青色、长虚线、+标记，图例中显示为“y=sin x”。
x1 = np.linspace(-2*np.pi,2*np.pi)
y1 = np.sin(x1)
plt.plot(x1,y1,color='g',marker='+',linestyle='--',label='y=sin(x)')
#（3）余弦曲线为品红色、短虚线、尖朝下的三角形标记，图例中显示为“y=cos x”。
y2 = np.cos(x1)
plt.plot(x1,y2,color='r',marker='v',linestyle=':',label='y=cos(x)')
#（4）正弦值+余弦值曲线为黑色、实线、正方形标记，图例中显示为“y=sin x+cos x”。
y3 = np.sin(x1) + np.cos(x1)
plt.plot(x1,y3,color='b',marker='s',linestyle='-',label='y=sin(x)+cos(x)')
#（5）制作图例，放在图形上部中间位置，图例要求无框，分别按（2）、（3）、（4）中要求设置标签。
plt.legend(loc='upper center',frameon=False)
#（6）设置y轴的刻度为[-2, -1, 0, 1, 2]，并画出刻度的网格线。
plt.yticks([-2,-1,0,1,2])
plt.grid(True)

# -----------------
# 制作x在[-10, 10]取值区间上的y=x^3+2x^2+3x+4函数、y的一阶导数和二阶导数的图形。要求
#（1）绘制三个子图，分别放置上述三个图形。
p1 = plt.figure(figsize=(10,8),dpi=80)
plt.xlim(-10,10)
x = np.linspace(-10,10,256)
#（2）第一个子图区域，标题为“原函数y”，使用红色实线绘制。
ax1 = p1.add_subplot(3,1,1)
y1 = x**3+2*x**2+3*x+4
plt.plot(x,y1,color='r',linestyle='-')
plt.title(label='原函数y') 
#（3）第二个子图区域，标题为“y的一阶导数”，使用蓝色虚线绘制。
ax2 = p1.add_subplot(3,1,2)
y2 = 3*x**2+4*x+3
plt.plot(x,y2,color='blue',linestyle='--')
plt.title(label='y的一阶导数')
#（4）第三个子图区域，标题为“y的二阶导数”，使用绿色实心原点绘制。
y3 = 6*x+4
ax3 = p1.add_subplot(3,1,3)
plt.plot(x,y3,color='g',linestyle='-')
plt.title(label='y的二阶导数')
#（5）设置三幅图的共同标题为“函数y及其一、二阶倒数”
plt.title(label='函数y及其一、二阶倒数')
plt.suptitle('函数y及其一、二阶导数')


# ------------------------
# 在同一副图中分别绘制为半径为2.5和3的两个圆，
# 填充两个圆形成的圆环，上半圆环用绿色填充，下半圆环用红色填充，填充时透明度设置为0.5。
r = [2.5,3]
x1 = np.linspace(-r[0],r[0],256)
x2 = np.linspace(-r[1],r[1],256)
y1 = np.sqrt(r[0]**2-x1**2)
y2 = np.sqrt(r[1]**2-x2**2)
plt.plot(x1,y1,'g',x1,-y1,'r')
plt.plot(x2,y2,'g',x2,-y2,'r')

plt.fill_between(x2,0,y2,facecolor='g',alpha=0.5)
plt.fill_between(x1,0,y1,facecolor='w')

plt.fill_between(x2,0,-y2,facecolor='r',alpha=0.5)
plt.fill_between(x1,0,-y1,facecolor='w')

plt.fill_between(x1,-y1,y1,facecolor='w')

# ---------------------
#某商品进价49元，售价75元，现在商场新品上架搞促销活动，顾客每多买一件就给优惠1%，但是每人最多可以购买30件。对于商场而言，活动越火爆商品单价越低，但总收入和盈利越多。对于顾客来说，虽然买的越多单价越低，但是消费总金额却是越来越多的，并且购买太多也会因为用不完而导致过期不得不丢弃造成浪费。现在要求计算并使用折线图可视化顾客购买数量与商家收益、顾客总消费以及顾客省钱情况的关系，并标记商场收益最大的批发量和商场收益。具体要求如下：
#（1）设置图例和网格线；
#（2）设置x轴取值为[0,30]；
#（3）分别如图设置x、y轴标签；
#（4）将商场收益最大的点用*表示，并标注利润的最大值。
plt.rcParams['font.sans-serif']='simhei'  #设置图中所有中文字体为黑体
c=49  #进价
p0=75  #初始售价
n=np.arange(31)  #顾客可购买的数量，0-30之间的整数
p=p0*(1-n*0.01)  #顾客购买数量n时的成交价
profit=n*(p-c)  #商家收益
consum=n*p  #顾客总消费
save=n*(p0-p)  #顾客省钱
plt.plot(n,profit,'r-',label='商家收益')   #r-表示红色的实现，label表示这条线表示商家收益，如果此处指定了label，图例中可以不指定
plt.plot(n,consum,'g:',label='顾客总消费')
plt.plot(n,save,'b-.',label='顾客省钱')
plt.legend()   #折线图中指定了label，图例中就不需要再指定图例的标签
plt.xlim(0,30)
plt.xlabel('顾客购买数量',fontsize=10)
plt.grid()  #可以显示网格
plt.ylabel('金额（元）')
plt.title('数量-金额关系图',fontproperties='stkaiti', fontsize=20)  #此处指定了字体，否则图中全部为黑体
maxprofit=profit.max()
bestNumber=profit.argmax()
#绘制最高利润的点，marker表示图形形状，s表示图形像素大小，c表示颜色
plt.plot(bestNumber,maxprofit,marker='*',c='r')
#标注箭头，xy表示箭头终点方向，text表示文本显示内容，xytext表示显示文本左下角的坐标，arrowprops表示箭头特性
plt.text(bestNumber-2,maxprofit+100,s=f'({bestNumber}, {maxprofit})')