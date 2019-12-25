#!/usr/bin/env python
# coding: utf-8

# In[6]:


var = 13
print(var)


# In[12]:


var1 = "Hello "
var2 = "Kritika!!"
message1 = var1+var2+ " How are you"
print(message1)


# In[16]:


message2= '{}{}How are you'.format(var1,var2)
print(message2)


# In[23]:


message3 = f'{var1}{var2}.How are you?'
print(message3)


# In[47]:


message4 = "Hello Kritika!!. How are you"
print(type(message4))
print(message4.lower())
print(message4.upper())
print(message4.__len__())
print(len(message4))
print(message4.count('!!'))
print(message4.find("Kritika"))
print(message4[6])
print(message4[0:14])
print(message4[2:-1])


# In[52]:


#loops
for i in range(0,7):
    print('value of i={}, squared  and cubed is {} and {} respectively'.format(i,i**2,i**3))
    print('inside loop')
print('outside loop')    
    


# In[65]:


#functions
def function1st():
    print("four type of functions")
    
#function1st()

#1)No argument No return type
def add():
    var1 = int(input("Enter value of num1"))
    var2 = int(input("Enter value of num2"))
    print(var1+var2)

#add()

#2)With argument No return type
def subtract(var1,var2):
    if(var1>var2):
        print(var1-var2)
    else:
        print(var2-var1)
        
#subtract(5,3)

#3) No argument with return type
def multiply():
    var1 = int(input("Enter value of num1"))
    var2 = int(input("Enter value of num2"))
    var3 = var1*var2
    return var3

#print(multiply())

#With argument with return type
def devide(var1, var2):
    return(var1/var2)

print(devide(57,7686))


# In[73]:


#input
"""name=input("Enter your name:")
print("Hello "+name)"""
"""var1=input("Enter the number:")
print(var1)
print(var1*2)
print(int(var1)*2)
print(type(var1))
print(type(int(var1)))"""

"""by default input function converts anything inputted to string
(also remember in python characters don't exist only strings exist )""" 


# In[85]:


#string splitting
print("Hi I am good,\nhow about you")
print("Column1 \tColumn2 \tColumn3 \tColumn4 \tColumn5")
print('Heyy What\'s up?')
print("Hey what\"s your name?")
print("What's your name?")
print("""triple quotes""")
print("""Hi I am good,
how about you""")

