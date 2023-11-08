#Class Library
import json

#Sample Data
data = {
    'name': 'AJ Savellano', 
    'age': 19,
    'city': 'Seattle, WA',
    'interests': ['Gaming is great','Fantasy Football King','Anime Enthusiast'],
    "is_student": True
}


#Writing data to a JSON file
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent=4)

print('Data has been written to JSON')


#Reading from JSON file
with open('data.json', 'r') as json_file:
    #Load the data
    loaded_data = json.load(json_file)

print('Data loaded from data.json')
print (loaded_data)


#Modify the data values
loaded_data['age'] = 21
loaded_data['interests'].append('I also like K-Pop')


#Write the modifications to the file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')

