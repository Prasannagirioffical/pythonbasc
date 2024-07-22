class person:
    def __init__(self, name, age, password) -> None:
        self.name = name
        self.age = age 
        self._password = password
        
    def get_password(self):
        return self._password
    
    def set_password(self, password):
        self._password = password 
    
    password = property(get_password, set_password)
        

person = person("ram", 12, "password")


person.set_password("123")
print(person.get_password())
