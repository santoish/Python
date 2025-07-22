"""  with open('Example.txt','w') as file:
    file.write('Hello World')

with open('Example.txt','r') as file:
    print(file.read())

with open('Example.txt','a') as file:
    file.write('1.Read all lines from the file.\n 2.Remove the lines you don’t want\n 3.Write the remaining lines back to the file.')

with open('Example.txt','r') as file:
    print(file.read())

import json

txt_data = 'I like Pizza'

file_path = 'D://Python//output.json'

employees = [
    {'id': '101', 'name': 'Sant', 'age': 19, 'course': 'BCA'},
    {'id': '102', 'name': 'Bala', 'age': 19, 'course': 'BCA'},
    {'id': '103', 'name': 'Sam', 'age': 19, 'course': 'BCA'},
]

with open(file_path,'w') as file:
    json.dump(employees,file,indent = 4)
    print(f'json file {file_path} was created')
 """
from tabulate import tabulate

data = [
    {'id': '101', 'name': 'Sant', 'age': 19, 'course': 'BCA'},
    {'id': '102', 'name': 'Bala', 'age': 19, 'course': 'BCA'},
    {'id': '103', 'name': 'Sam', 'age': 19, 'course': 'BCA'},
]
print(tabulate(data, headers="keys", tablefmt="grid"))

