
# coding: utf-8

# In[3]:

#https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
get_ipython().magic('matplotlib inline')
np.set_printoptions(precision=5, suppress=True)


# In[16]:

hd= []
h = open("Desktop\hd1.txt","r")
for row in h:
    row = row.split()
    hd.append(row)
print(hd)


# In[20]:

Z = linkage(hd)


# In[21]:

print(Z[:10])


# In[23]:

print(Z[275:])


# In[40]:

plt.figure(figsize=(15, 4))
plt.title('Hierarchical Clustering Q1')
plt.xlabel('data instance index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=6.,  # font size for the x axis labels
)
plt.show()


# In[ ]:



