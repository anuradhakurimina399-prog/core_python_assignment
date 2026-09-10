#!/usr/bin/env python
# coding: utf-8

# In[1]:


def search_patients(patients, disease):
    result = []

    for patient in patients:
        if patient["Disease"] == disease:
            result.append(patient["Name"])

    return result


patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

result = search_patients(patients, search_disease)

print("Patients with", search_disease + ":", result)


# In[ ]:




