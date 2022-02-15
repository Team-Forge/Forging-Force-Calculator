#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[3]:


print('''Forging Force Calculater\n
It calculates the force required for forging.''')
print("\n")
print("\n")
print("\n")
#here we are going to calculate the force required for forging

print('''The General Formula is : F= p*A*ȣ \n
Where :  
F= Forging Force\n
p= Specific pressure on forging component at the final forging phase\n
A= Surface of forging component projection on dividing plane\n
ȣ= Coefficient of forging force increase due to formation on forging component ring''')

print('''To Calculate the Force Please input the following:''')
p = float(input("Enter the specific pressure p : "))
a = float(input("Enter the surface of forging component A : "))
r = float(input("Enter the Coefficient of forging force ȣ : "))
f= p*a*r
print("The fore required for forging is: ",f)


# In[ ]:




