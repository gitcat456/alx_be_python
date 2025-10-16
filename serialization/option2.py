import pickle

# Sample Python object
data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

# Serialize the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)