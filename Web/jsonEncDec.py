import json

'''
json.dumps()
This function is used to serialize a Python object into a JSON string. The dumps() function takes a single argument, the Python object, and returns a JSON string.

json.loads()
This function is used to parse a JSON string into a Python object. The loads() function takes a single argument, the JSON string, and returns a Python object.

json.dump()
This function is used to serialize a Python object and write it to a JSON file. The dump() function takes two arguments, the Python object and the file object. 

# serialize Python object and write to JSON file
python_obj = {'name': 'John', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(python_obj, file)

 json.load()
 This function is used to read a JSON file and parse its contents into a Python object. The load() function takes a single argument, the file object, and returns a Python object.  

  # read JSON file and parse contents
with open('data.json', 'r') as file:
    python_obj = json.load(file)
print(python_obj)    

'''





person = '{"currencyCode":"CZK","customerCode":"C50BF1", "quantityLines": [{"towKod":"C50BF1", "quantitiy":1}]}'
person_dict = json.loads(person)
print(person_dict)
