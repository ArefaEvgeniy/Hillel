import pickle


with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

print(data)
print(data[-1].get_age())
