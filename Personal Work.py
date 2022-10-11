#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Question 1
#print all element in a list using for loop

cars = ['Honda','Toyota','Benz', 'Nissan','Ferarri']
for y in cars:
    print(y)


# In[32]:


#Question 2
#Using range (1,101), make two list, one containing all even numbers and other containing all odd numbers.

odd_numbers =[]
even_numbers =[]
for x in range(1,101):
    if x%2 == 0:
        odd_numbers.append(x)
    else:
        even_numbers.append(x)
print(odd_numbers)
print(even_numbers)


# In[ ]:


#question 3
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their 
salary and year of service and print the net bonus amount.

benchmark = 5
def incentive(salary, serviceYear):
    if serviceYear > benchmark:
        bonus = 0.05*salary
        print (bonus)
        return  bonus
    else:
        print('no bonus')
    


# In[8]:


salary = input('How much do you earn')
yearsOfService = input('How long have you served')

incentive(int(salary),int(yearsOfService))


# In[36]:


#Question 4
age1 = (input('How old are you'))
age2 = (input('How old are you'))
age3 = (input('How old are you'))
maxage = max(age1, age2, age3)
miniage = min(age1, age2, age3)
print('youngest age is:', miniage)
print('oldest age is:', maxage)


# In[24]:


#question 5
def Grade(mark):
    if mark < 25:
        print('F')
    elif mark >25 and mark <=45:
        print('E')
    elif mark >45 and mark <=50:
        print('D')
    elif mark >50 and mark <=60:
        print('C')
    elif mark >60 and mark <=80:
            print('B')
    else:
        print('A')


# In[25]:


mark = input('what was your mark')

Grade(int(mark))


# In[37]:


#Question 6
#write a python script to merge two python dictionaries

cars = {'Honda' : 'red', 'Toyota' : 'blue', 'Benz' : 'black'}
schools = {'OAU' : 'federal', 'OOU' : 'state', 'BOWEN' : 'private'}

total = cars.copy()
total.update(schools)

print(total)


# In[40]:


#Question 7
#write a python program to remove a key from a dictionary'

industries= {'Nigeria' : 'Nollywood', 'America' : 'Hollywood', 'India' : 'Bollywood'}
industries.pop('Nigeria')
print(industries)


# In[15]:


list1 = [10, 20, 30, 40, 50, 60, 100]
print('largest number is:', max(list1))


# In[ ]:




