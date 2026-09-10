#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_total(cart_items):
    if len(cart_items) == 0:
        return 0

    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total = total - (total * 0.10)

    return total


cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}

total_price = calculate_total(cart_items)

if total_price == 0:
    print("Cart is empty")
else:
    print("Total Price:", total_price)


