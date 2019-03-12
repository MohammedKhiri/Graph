import pandas as pd
import matplotlib.pyplot as py
from matplotlib import style

data={'day':['mon','Tus','Wed'],
      'sleping':[12,6,8],
      'Exercise':[56,45,57],
      'Working':[6,8,13]
      }

print(data)

ps=pd.DataFrame(data)
print(ps)
#######################
a=['mohammed','ali','noor']
pm=pd.DataFrame(a)
print(pm)
#######################
a=[1,2,3]
pm=pd.DataFrame(a)
print(pm)
###################
print(style.available)
style.use('seaborn-darkgrid')
ps['Exercise'].plot()
py.show()


#####################
pf=pd.read_csv('d:\ABC.csv')
print(pf)

print(pm)
pm.columns=['mark']
print(pm)
pm['new mark']=60
print(pm)
pm['new col']=pm['mark']+7
print(pm)
pm['new city']=1
print(pm)

