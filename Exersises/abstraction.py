""" from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self,user):
        self.userName = user

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class CreditCard(Payment):
    def __init__(self, user):
        super().__init__(user)

    def pay(self,amt):
        print(f'Rs.{amt} Paid using Credit Card by {self.userName}')

    def refund(self,amt):
        print(f'Rs.{amt} refunded using Credit Card by {self.userName}')
        
p1 = CreditCard("Arjun")
p1.pay(1000)
p1.refund(200)
 """
#2
""" from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.userName = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,base,bonus):
        super().__init__(name)
        self.base_salary = base
        self.bonus_salary = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus_salary
    
    def get_details(self):
        return (f'Full - Time Employee {self.userName} - Salary : Rs. {self.calculate_salary()}')
    
class PartTimeEmployee(Employee):
    def __init__(self,name,base,hours):
        super().__init__(name)
        self.base_salary = base
        self.work_hours = hours

    def calculate_salary(self):
        return self.base_salary * self.work_hours
    
    def get_details(self):
        return (f'Full - Time Employee {self.userName} - Salary : Rs. {self.calculate_salary()}')
    
e1 = FullTimeEmployee("Alice", 50000, 10000)
e2 = PartTimeEmployee("Bob", 1000, 20)

print(e1.get_details())  # Alice: ₹60000
print(e2.get_details())  # Bob: ₹20000 """

#3

""" from abc import ABC, abstractmethod

class Shipping(ABC):


    @abstractmethod
    def calculate_cost(self):
        pass

class StandardShipping(Shipping):
    def calculate_cost(self,weight):
        return (weight * 10) + 50

class ExpressShipping(Shipping):
    def calculate_cost(self,weight):
        return (weight * 20) + 100
    
ship1 = StandardShipping()
ship2 = ExpressShipping()

print(ship1.calculate_cost(5))
print(ship2.calculate_cost(5)) """

#4
""" from abc import ABC,abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class ExcelReport(Report):
    def generate(self,data):
        # print(da)
        print(f'Generating Excel report with data: {data}')
    
class PDFReport(Report):
    def generate(self,data):
        print(f'Generating PDF report with data: {data}')
    
r = ExcelReport()
r.generate({"sales": 10000})
r1 = PDFReport()
r1.generate({"sales": 20000}) """

#5
""" from abc import ABC, abstractmethod

class Ride(ABC):
    @abstractmethod
    def calculate_fare(self):
        pass

class BikeRide(Ride):
    def calculate_fare(self,distance):
        return distance * 5
    
class AutoRide(Ride):
    def calculate_fare(self,distance):
        return (distance * 7) + 20
    

r1 = BikeRide()
r2 = AutoRide()

print(r1.calculate_fare(10))
print(r2.calculate_fare(10)) """

#6

from abc import ABC, abstractmethod

class Bill(ABC):
    def __init__(self,amt):
        self.amount = amt

    @abstractmethod
    def calculate_total(self):
        pass

class PremiumCustomer(Bill):
    def __init__(self, amt):
        super().__init__(amt)

    def calculate_total(self):
        self.discount_price = self.amount * (10/100)
        self.amount -= self.discount_price
        return self.amount
    
class VIPCustomer(Bill):
    def __init__(self, amt):
        super().__init__(amt)

    def calculate_total(self):
        self.discount_price = self.amount * (0/100)
        self.amount -= self.discount_price
        return self.amount
    
b1 = PremiumCustomer(1000)
b2 = VIPCustomer(2000)

print(b1.calculate_total())  # 900
print(b2.calculate_total())  # 1600

