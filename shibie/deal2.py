import pandas as pd
def deal2():
    data = pd.read_excel('data.xlsx')
    print('正在进行特征的去零处理...')
    data['备用整形3'] = data['备用整形3'] + 2
    data['备用整形4'] = data['备用整形4'] + 2
    data['备用整形5'] = data['备用整形5'] + 1
    data['备用整形6'] = data['备用整形6'] + 1
    data.to_excel('mydata.xlsx',index=False)
    print('特征的去零处理完成,保存在mydata.xlsx！')