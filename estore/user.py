class User:
    def __init__(self, age,email,address,name, password, phoneNumber):
        self.age = age
        self.email = email
        self.address = address
        self.name = name
        self.password = password
        self.phoneNumber = phoneNumber

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
        

