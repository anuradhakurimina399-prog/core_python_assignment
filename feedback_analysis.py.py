#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def positive_feedback_percentage(ratings):
    if len(ratings) == 0:
        return 0

    positive_count = 0

    for rating in ratings:
        if rating == 4 or rating == 5:
            positive_count += 1

    percentage = (positive_count / len(ratings)) * 100

    return percentage


ratings = [5, 4, 3, 5, 2, 4, 1, 5]

result = positive_feedback_percentage(ratings)

print("Positive Feedback:", result, "%")

