#!/usr/bin/env python
# coding: utf-8

# In[1]:


def book_seat(booked_seats, seat):
    if seat in booked_seats:
        print("Seat", seat, "is already booked")
    else:
        booked_seats.append(seat)
        print("Seat", seat, "booked successfully")


def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        print("Seat", seat, "cancelled successfully")
    else:
        print("Seat", seat, "is not booked")


total_seats = 10
booked_seats = [2, 5, 7]

book_seat(booked_seats, 3)

cancel_seat(booked_seats, 5)

available_seats = []

for seat in range(1, total_seats + 1):
    if seat not in booked_seats:
        available_seats.append(seat)

print("Available seats:", available_seats)


# In[ ]:




