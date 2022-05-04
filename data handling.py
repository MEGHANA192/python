#!/usr/bin/env python
# coding: utf-8

# In[6]:


#to read a file
f=open("D:\\puppy.txt","r")
print(f.read())
f.close()


# 

# In[7]:


#to reaqd a file upto a certain extent
f=open("D:\\puppy.txt","r")
print(f.read(7))
f.close()


# In[9]:


#read line by line
f=open("D:\\puppy.txt","r")
print(f.readline())
print(f.readline())
f.close()


# In[14]:


#adding to a file
f=open("D:\\puppy.txt","a")
f.write("\nhi how are you\nwhere do you live?")
f.close()


# In[17]:


#when u give w olny that line will be printed
f=open("D:\\puppy.txt","w")
f.write("hi how are you")
f.close()
f=open("D:\\puppy.txt","r")
print(f.read())
f.close()


# In[19]:


#how to copy a file from one file to another file
f=open("D:\\puppy.txt","r")
b=f.readlines()
f.close()
f1=open("D:\\puppy1.txt","w")
f1.writelines(b)
f1.close()
f2=open("D:\\puppy1.txt","r")
for i in f2:
    print(i)
f2.close()


# In[25]:


#creating  a  file using x
f=open("D:\\puppy6.txt","x")
f.close()


# In[23]:


#creatin a file and writing in that file
f=open("D:\\puppy4.txt","w")
f.write("i love momos")
f.close()


# In[24]:


#creating a file and copying content from other file
f=open("D:\\puppy4.txt","r")
b=f.readline()
f.close()
f1=open("D:\\puppy5.txt","w")
f1.writelines(b)
f1.close()


# In[ ]:




