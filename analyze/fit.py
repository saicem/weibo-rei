import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

data_file = '.\\W_data.csv'

datasets_X = []
datasets_Y1 = []
datasets_Y2 = []

X = []
Y1 = []
Y2 = []
#处理异常缺失值
dataset = pd.read_csv(data_file, delimiter=',', na_values='?', header=None)   
for i in range(len(dataset)-1):
    if pd.notna(dataset.iloc[i+1][2]):    #判断传入参数是否为nan
        datasets_X.append( int(dataset.iloc[i+1][1]))# 'comment_num'
        datasets_Y1.append(int(dataset.iloc[i+1][2]))# 'like_num'
        datasets_Y2.append(int(dataset.iloc[i+1][3]))# 'repost_num'
        X.append(datasets_X[-1])       #画图的点
        Y1.append(datasets_Y1[-1])
        Y2.append(datasets_Y2[-1])

length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length,1])   #转化成numpy数组
datasets_Y1 = np.array(datasets_Y1)
datasets_Y2 = np.array(datasets_Y2)
poly_reg = PolynomialFeatures(degree = 2)   #多项式拟合的阶数
X_poly = poly_reg.fit_transform(datasets_X)   #转化成可以拟合的数据
lin_reg_1 = linear_model.LinearRegression()  #生成线性拟合器
lin_reg_2 = linear_model.LinearRegression()
lin_reg_1.fit(X_poly, datasets_Y1)#拟合
lin_reg_2.fit(X_poly, datasets_Y2)
#预测缺失数据并更新到读取的数据中
for i in range(len(dataset)):
    if not pd.notna(dataset.iloc[i][2]):#'like_num'
        dataset.iloc[i][2] = int(lin_reg_1.predict(\
            poly_reg.fit_transform(np.array(int(dataset.iloc[i][1])).reshape(-1, 1)))[0])
        dataset.iloc[i][3] = int(lin_reg_2.predict(\
            poly_reg.fit_transform(np.array(int(dataset.iloc[i][1])).reshape(-1, 1)))[0])
        X.append(int( dataset.iloc[i][1]))
        Y1.append(int(dataset.iloc[i][2]))
        Y2.append(int(dataset.iloc[i][3]))
        
dataset.columns = ['id','comment_num','like_num','repost_num']
dataset[1:].to_csv('W_data_p.csv')# 保存到文件

#### 下面是绘图
minX = min(X)
maxX = max(X)
x = np.arange(minX,maxX).reshape([-1,1])

nRow =1
nCol =2
str_xlable = "comment_num"
plt.subplot(nRow,nCol,1)
plt.scatter(X, Y1, color = 'blue')
plt.plot(x,  lin_reg_1.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.xlabel(str_xlable)
plt.ylabel('like_num')

plt.subplot(nRow,nCol,2)
plt.scatter(X, Y2, color = 'red')
plt.plot(x,  lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'red')
plt.xlabel(str_xlable)
plt.ylabel('repost_num')
plt.show()
#plt.savefig('test.png')