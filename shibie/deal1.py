import pandas as pd
import numpy as np
def deal1():
    data = pd.read_csv('event.csv',encoding='gb18030')
    print('正在进行特征的选择和提取...')
    data['备用整形3'] = pd.factorize(data['操作'])[0].astype(np.int16)
    data['备用整形4'] = pd.factorize(data['事件原始类型'])[0].astype(np.int16)
    data['备用整形5'] = pd.factorize(data['事件原始等级'])[0].astype(np.int16)
    data['备用整形6'] = pd.factorize(data['目的端口'])[0].astype(np.int16)
    data['备用长整形3']=pd.factorize(data['事件类型'])[0].astype(np.uint16)

    mydata = data.iloc[:,52:57]
    mydata.to_excel('data.xlsx',index=False)
    print('特征的选择和提取成功，保存在data.xlsx!')
