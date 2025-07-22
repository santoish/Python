""" from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCard(Payment):
    def process_payment(self,amount):
         print(f'Processing Rs.{amount} through Credit Card')
    
class UPI(Payment):
    def process_payment(self,amount):
         print(f'Processing Rs.{amount} through UPI')
    
class PayPal(Payment):
    def process_payment(self,amount):
         print(f'Processing Rs.{amount} through PayPal')
    
payments = [CreditCard(), UPI(), PayPal()]
for p in payments:
    p.process_payment(1000)
 """
#2
""" from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def honk(self):
        pass

class Car(Vehicle):
    def honk(self):
        print('Car Honks : Beep !')

class Bike(Vehicle):
    def honk(self):
        print('Bike Honks : Peep !')

class Truck(Vehicle):
    def honk(self):
        print('Truck Honks : Hoonk !')

vehicles = [Car(), Bike(), Truck()]
for v in vehicles:
    v.honk() """

from abc import ABC, abstractmethod

#3
""" class Files(ABC):
    @abstractmethod 
    def export(self):
        pass

class PDF(Files):
    def export(self,data):
        print(f'Exporting {data} as PDF')
class Word(Files):
    def export(self,data):
        print(f'Exporting {data} as Word')
class ExcelSheet(Files):
    def export(self,data):
        print(f'Exporting {data} as ExcelSheet')

files = [PDF(), Word(), ExcelSheet()]
for f in files:
    f.export("report") """

#4

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self,msg):
        print(f'Sending Email: {msg}')
class SMS(Notification):
    def send(self,msg):
        print(f'Sending SMS: {msg}')
class Push(Notification):
    def send(self,msg):
        print(f'Sending Push Notification: {msg}')

messages = [Email(), SMS(), Push()]
for m in messages:
    m.send("Your OTP is 1234")
