# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:14:04 2019

@author: Mohammed
"""

import pandas as pd
import matplotlib.pyplot as py


data={'x':[1,2,3,4,5],
      'y':[2,4,5,4,5]
      }

ps=pd.DataFrame(data)
print(ps)
manx=ps['x'].mean()
many=ps['y'].mean()
print(manx)
print(many)

ps['x-xx']=ps['x']-manx
ps['y-yy']=ps['y']-many
print(ps)

ps['X-xx^2']=ps['x-xx']**2
print(ps)

ps['x-xx,y-yy']=ps['x-xx']*ps['y-yy']
print(ps)

b1=sum(ps['x-xx,y-yy'])/sum(ps['X-xx^2'])
print(b1)
b0=many-b1*manx
print(b0)
ps['y^']=b0+b1*ps['x']
print(ps)

py.scatter(ps['x'],ps['y'])

py.plot(ps['x'],ps['y^'])
py.show()



