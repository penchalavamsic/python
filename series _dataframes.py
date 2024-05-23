import numpy as np
import pandas as pd
arr1=np.array([1,2,3])# it shloud be 1-D array only
a=pd.Series(arr1)
print(a) 
dt={                #using dataframes with heterogenous data
    'Name':['Vamsi','Hello'],
    'Age':[14,5]
}
b=pd.DataFrame(dt)
print(b)
