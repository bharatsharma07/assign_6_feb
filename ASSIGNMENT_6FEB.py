#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ANSWER 1
def product_of_numbers(lst):
    flat_list=[]
    for item in lst:
        if isinstance(item,list):
            flat_list.extend(item)
        elif isinstance(item,dict):
            for value in item.values():
                if isinstance(value,(int,float)):
                    flat_list.append(value)
        else:
            flat_list.append(item)
    product=1
    for num in flat_list:
        if isinstance(num,(int,float)):
            product*=num
    return product
list1=[1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'machine learning']
result=product_of_numbers(list1)
print(result)


# In[2]:


def encrypt_message(message):
    encrypted_message = ""
    for char in message.lower():
        if char.isalpha(): 
            encrypted_char = chr(ord('a') + (ord('z') - ord(char)))
            encrypted_message += encrypted_char
        elif char == ' ':
            encrypted_message += '$' 
        else:
            encrypted_message += char
    return encrypted_message

input_sentence = "I want to become a Data Scientist."
encrypted_sentence = encrypt_message(input_sentence)
print(encrypted_sentence)


# In[ ]:




