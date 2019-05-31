#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import PIL
from PIL import Image
import hashlib
import glob


# In[9]:


def dhash (image, hash_size):

    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS)
    
    pixels = list(image.getdata())

    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)  

    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        
        if value:
            decimal_value += 2**(index % 6)
        if (index % 6) == 5:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0
    
    return ''.join(hex_string)


# In[10]:


def hamdistanse (str1, str2):
    diffs = 0
    for ch1, ch2 in zip (str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs


# In[14]:


def similarity (folder):
    list_hash = []
    list_dhash = []
    list_name = []
    
    main_dict = {}
    for f in glob.glob(folder + '/*.jpg'):
        
        image_open = Image.open(f)
        image_dhash = dhash(image_open, hash_size = 6)
        list_dhash.append(image_dhash)
        
        head, tail = os.path.split(f)
        list_name.append(tail)
  
    i = 0
    j = 0
    
    for i in range(len(list_name)):
        for j in range(i + 1, len(list_name)):
            
            if hamdistanse(list_dhash[i], list_dhash[j]) < 6:
                print (list_name[i] + ' ' +  list_name[j])         
            else:
                continue


# In[19]:


folder_path = input("Enter the path to the folder: ")


# In[20]:


similarity (folder_path)


# In[ ]:




