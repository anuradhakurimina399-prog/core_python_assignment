#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10

    total = base_fare + (distance * distance_fare)

    return total


trips = [5, 10, 3]

total_fare = 0

for i in range(len(trips)):
    fare = calculate_fare(trips[i])

    print("Trip", i + 1, ": $", fare)

    total_fare += fare

print("Total Fare: $", total_fare)

