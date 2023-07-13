import pickle

big_data = [0, []]

in_bytes = pickle.dumps(big_data)
print(in_bytes)
in_standatr = pickle.loads(in_bytes)
print(in_standatr)

with open('big_obj.data', 'wb') as file:
    pickle.dump(big_data, file)

with open('big_obj.data', 'rb') as file:
    in_standatr = pickle.load(file)

print(in_standatr)