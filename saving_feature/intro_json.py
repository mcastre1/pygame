import json

data = {
    'Germany' : 'Berlin',
    'UK' : 'London',
    'China' : 'Beijin',
    'Kitten' : 123
}

# Write json text file from python dictionary
with open('./saving_feature/test_data.txt', 'w') as test_file:
    json.dump(data, test_file)

# Read json text file and convert it into python dictionary
with open('./saving_feature/test_data.txt', 'r') as test_file:
    data2 = json.load(test_file)

print(data2)