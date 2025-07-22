""" class Student:
    def __init__(self,sName):
        self.__student_name = sName
        self.__courses = []


    def register_course(self,cName):
        if cName in self.__courses:
            print(f'{cName} is Already Added')
        else:
            self.__courses.append(cName)

    def remove_course(self,cName):
        self.__courses.remove(cName)
        print(f'{cName} Have been Removed')

    def get_courses(self):
        return (self.__courses)

s = Student("Anu")
s.register_course("Math")
s.register_course("Physics")
s.register_course("Math")  # Duplicate
s.remove_course("Math")
print(s.get_courses())
 """

#2
"""class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self,item_name,item_qty):
        if item_name in self.__items:
            self.__items[item_name] += item_qty
        else:
            self.__items[item_name] = item_qty
        # print(self.__items)

    def remove_item(self,item_name,item_qty):
        if item_name in self.__items:
            self.__items[item_name] -= item_qty
            # print(self.__items)

    def get_total_items(self):
        self.__total = sum(self.__items.values())
        return self.__total
    
    def get_items(self):
        return self.__items


cart = ShoppingCart()
cart.add_item("Laptop", 1)
cart.add_item("Mouse", 2)
cart.add_item("Mouse", 2)
cart.remove_item("Mouse", 1)
print(cart.get_items()) 
print(cart.get_total_items()) """

#3

""" class LeaveTracker:
    def __init__(self,eName,lCount):
        self.emp_name = eName
        self.__leave_balance = lCount

    def apply_leave(self,leaveCount):
        if leaveCount <= self.__leave_balance:
            print(f'Leave approved for {leaveCount} days')
            self.__leave_balance -= leaveCount
        else:
            print(f'Insufficient Leave Balance')

    def get_balance(self):
        if self.__leave_balance <= 15:
            return self.__leave_balance
        


emp = LeaveTracker("Ravi", 15)
emp.apply_leave(5)
emp.apply_leave(11)
print(emp.get_balance()) """

#4

""" class Vehicle : 
    def __init__(self,type_vechicle):
        self.vechicle = type_vechicle
        self.__fuel = 0

    def add_fuel(self,lr):
        if self.__fuel > 0:
            self.__fuel += lr
        else:
            self.__fuel = lr 
        print(f'{lr} Ltr Fuel Added')

    def drive(self,distance):
        if self.__fuel * 10 >= distance:
            print(f'You Drove {distance}km')
            self.__fuel -= (distance/10)

        else:
            print(f'Not Enough Fuel')

    def get_fuel(self):
        return self.__fuel

v = Vehicle("Car")
v.add_fuel(10)
v.drive(50)
v.drive(100)
v.add_fuel(10)

print(v.get_fuel()) """

#5

class Bill:
    def __init__(self,amt):
        self.__amount = amt
    
    def apply_discount(self,percent):
        if(percent < 50):
            self.__discount_price = self.__amount * (percent / 100)
            self.__amount -= self.__discount_price

        else:
            print(f'Discount must be between 0 and 50%')

    def get_final_amount(self):
        return self.__amount
    

b = Bill(1000)
b.apply_discount(20)
print(b.get_final_amount())  # 800.0

b.apply_discount(60)         # Invalid
