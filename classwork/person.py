import address

class Person:
    def __init__(self, name, age,dob,phoneNumber,gender,number,street,city,state):
        self.__name = name
        self.__age = age
        self.__dob = dob
        self.__phoneNumber = phoneNumber
        self.__gender = gender
        self.__address = address.Address(number,street,city,state)

    def get_name(self):
            return self.__name

    def get_age(self):
            return self.__age

    def greet(self):
            return "Hello " + self.__name

    def set_age(self, age):
        self.__age = age
        if self.__age < 0:
            raise ValueError("please enter a valid age.")





