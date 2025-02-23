#%%
import numpy as np
import seaborn as sns
from seaborn import histplot
#%%
# seaborn.displot(a,bins=None,hist=True,kde=True,rug=True,fit=None,color=None)
#%% md
# 上述函数中常用参数的含义如下：<br>
# (1)a:表示要观察的数据，可以是Series，一堆数组或列表<br>
# (2)bins:用于控制条形的数量<br>
# （3）hist：接收布尔类型，表示是否绘制（标注）直方图
# 
#%%
np.random.seed(22)
arr=np.random.randn(100)
sns.histplot(arr,bins=100)

#%%
