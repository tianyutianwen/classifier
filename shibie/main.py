import pandas as pd
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy
import deal1
import deal2

def main():
    #读取数据集X和y
    X_data = pd.read_excel('mydata.xlsx',usecols=[0,1,2,3])
    X = X_data.values.tolist()
    y_data = pd.read_excel('mydata.xlsx',usecols=[4])
    y = y_data.values.tolist()
    #数据集的划分
    print('正在进行数据集的划分...')
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
    print('数据集划分完成！')
    # 神经网络
    print('正在进行训练...')
    model = MLPClassifier(activation='tanh', solver='adam', alpha=0.0001,max_iter=200)
    model.fit(X_train,y_train)
    print('训练完成！')
    print('正在进行测试集的预测...')
    predict=model.predict(X_test)
    print('预测完成，预测结果如下：')
    print(predict)  #预测值
    print('真实数据如下：')
    print(y_test)   #真实值
    #打印准确率
    print('神经网络分类准确率:{:.3f}'.format(model.score(X_test, y_test)))

if __name__ == '__main__':
    deal1.deal1()
    deal2.deal2()
    main()