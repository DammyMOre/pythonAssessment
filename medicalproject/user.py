
import address

class User:
    def __init__(self, name,age, gender,phone_number,house_number,street,city,state):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone_number = phone_number
        self.__address = address.Address(house_number,street,city,state)


    def get_name(self):
        return self.__name

    def validate_age(self,age:int) -> int:
        if self.__age < 0:
            raise ValueError("Please enter a valid age")
        return age

    def set_age(self, age)-> None:
        self.__age = self.validate_age(age)

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_phone_number(self):
        return self.__phone_number


