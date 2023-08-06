#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
import os


# In[8]:


categorys = os.listdir()
categorys


# In[9]:


categorys.pop()


# In[11]:


#integer_to_class = {'0': 'meningioma (0)', '1': 'glioma (1)', '2': 'pituitary tumor (2)'}
label = [1,0,3,2]


# In[13]:


labels =[]
data = []
for i in range(1,5):
    imagesnames = os.listdir(categorys[i])
    for imagename in imagesnames:
        labels.append(label[i-1])
        imagepath = os.path.join(categorys[i],imagename)
        img=cv2.imread(imagepath)
        grayimage =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(grayimage,(512,512))
        data.append(resized)


# In[23]:


data = np.array(data)
file_name ="data.npy"
np.save(file_name, data)


# In[22]:



import numpy as np
labels = np.array(labels)
file_name = "labels.npy"
np.save(file_name, labels)


# In[17]:


import matplotlib.pyplot as plt


# In[19]:


plt.imshow(data[1],cmap= 'gray')


# In[ ]:




