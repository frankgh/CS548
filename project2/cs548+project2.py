
# coding: utf-8

# In[27]:

import csv
f = open("Desktop\credit.csv")
cf = csv.reader(f)


# In[28]:

fl=[]
for row in cf:
    fl.append(row)


# In[29]:

len(fl)


# In[30]:

fl=fl[2:]
len(fl)


# In[31]:

fw = []
for line in fl:
    for j in line:
        j=float(j)
        fw.append(j)
len(fw)


# In[35]:

missing = []
for entry in fw:
    if entry <-1:
        missing.append(entry)
len(missing)


# In[36]:

print(missing)


# In[52]:

import numpy
nf = numpy.array(fw)
shape=(30000,25)
nf.reshape(shape)


# In[41]:

nf


# In[54]:

type(nf[1])


# In[55]:

import pandas
from sklearn import tree


# In[56]:

model = tree.DecisionTreeClassifier(criterion = 'gini') #or entropy
model = tree.DecisionTreeRegressor() 
model.fit(x,y) #for x predictor and y target


# In[ ]:



