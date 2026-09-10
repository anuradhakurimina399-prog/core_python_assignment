#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_item(menu, item):
    menu.append(item)


def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(item, "does not exist in the menu")


def check_item(menu, item):
    if item in menu:
        return item + " is available"
    else:
        return item + " is not available"


menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item(menu, "Tacos")

remove_item(menu, "Salad")

result = check_item(menu, "Pizza")

print("Updated menu:", menu)
print("Availability:", result)


# In[ ]:




