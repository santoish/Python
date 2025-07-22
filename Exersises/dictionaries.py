""" fields = ['id', 'name', 'email']
data = [1, 'John Doe', 'john@example.com']
final_data = {}

for i in range(3):
    final_data[fields[i]] = data[i]

print(final_data)

#2

orders = ['apple', 'banana', 'apple', 'mango', 'banana', 'apple']

data = {}

for i in orders:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(data)  """

""" students = [{ "ID" : 101, "Name" : "Sant"},
           { "ID" : 102, "Name" : "Bala"},
           { "ID" : 103, "Name" : "Sam"}]

if not students:
    print('Aama')
del students
print(students) """
num = '1'
num1 = int(num)
print(type(num1))