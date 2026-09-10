#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_average(marks):
    return sum(marks) / len(marks)


students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages = {}

for name in students:
    average = calculate_average(students[name])
    averages[name] = round(average, 2)

top_performer = max(averages, key=averages.get)

print("Average Marks:", averages)
print("Top Performer:", top_performer)


# In[ ]:




