#simple json

import json
data = {
	"president": {
		"name": "Joe Biden",
		"species": "homo"
	}
}
print(f'*** work with json ***')
print(f'simple data: {data}')

print(f'\nstart serialization in file:')
with open("C:\\proj_2023\\PeEx\\smallPythonProgram\\serialization\\small_file.json", "w") as write_file:
	json.dump(data, write_file)
print(f'serialization in file was done (please check the file)')

print(f'\nstart serialization in string: ')
json_string = json.dumps(data)
print(f'serialization in string was done: {json_string}')

print(f'\nstart deserialization from file:')
with open("C:\\proj_2023\\PeEx\\smallPythonProgram\\serialization\\small_file.json", "r") as read_file:
	data_read_file = json.load(read_file)
	print(f'deserialization from file was done: {data_read_file}')
	print(f'type result field: {type(data_read_file)}')

print(f'\nstart deserialization from string:')
data_read_string = json.loads(json_string)
print(f'deserialization from string was done')
print(f'result type: {type(data_read_string)}, result data: {data_read_string}')


#simple 
import pickle

print(f'\n*** work with pickle ***')
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f'name: {self.name} | age: {self.age} '

# create object
obj = Person("Timoti", 35)
print(f'object: {obj}')

print(f'\nstart serialization object in string')
serialized_obj_1 = pickle.dumps(obj)
#serialized_obj_2 = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
print(f'serialization object in string was done')
print(f'str: {serialized_obj_1}, type: {type(serialized_obj_1)}')

print(f'\nstart serialization in file')
with open('C:\\proj_2023\\PeEx\\smallPythonProgram\\serialization\\serialized_object.pkl', 'wb') as file:
	pickle.dump(obj, file)
print(f'serialization in file was done (please check the file)')

print(f'\nstart deserialization from string:')
deserialized_obj = pickle.loads(serialized_obj_1)
print(f'deserialization from file was done')
print(f'object: {deserialized_obj}, type: {type(deserialized_obj)}')

print(f'\nstart deserialization from file:')
with open('C:\\proj_2023\\PeEx\\smallPythonProgram\\serialization\\serialized_object.pkl', 'rb') as file:
	loaded_obj = pickle.load(file)
	print(f'deserialization from file was done')
	print(f'object: {loaded_obj}, type: {type(loaded_obj)}')
