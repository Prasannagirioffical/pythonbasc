# class Grandfather:
#     house = "luxury house"
    
# class Father(Grandfather):
#     car = "land crusior"
 
# class Mother:
#     jweleary = "gold"
    
# class Son(Father, Mother):
#     console = "ps5"
    
    
# son = Son()
#  print(son.house)
#  print(son.car)
#  print(son.console)
class Person:
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary 
        
    
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.salary == other.salary

ram = Person("Ram", 24, 123)
shyam = Person("shyam", 3, 123)
print(ram == shyam)
