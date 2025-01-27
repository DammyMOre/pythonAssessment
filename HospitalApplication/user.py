from pythonAssessment.HospitalApplication.address import Address


class User:
    def _init_(self, name, age, number, street, city, state, gender, phone):
        self.__name = name
        self.age = self.validate_age(age)
        self.__address = Address(number, street, city, state)
        self.__gender = self.validate_gender(gender)
        self.__phone = phone

    def get_name(self):
        return self.__name

    def validate_age(self, age: int) -> int:
        if age < 0:
            raise ValueError("Age must be greater than or equal to zero")
        return age

    def set_age(self, age: int) -> None:
        self.age = self.validate_age(age)

    def get_age(self) -> int:
        return self.age

    def get_address(self) -> Address:
        return self.__address

    def validate_gender(self, gender: str) -> str:
        valid_genders = {"Male", "Female"}
        if gender.capitalize() not in valid_genders:
            raise ValueError("Gender must be 'Male' or 'Female'")
        return gender.capitalize()

    def get_gender(self) -> str:
        return self.__gender

    def _str_(self):
        return f"""
        Name: {self.__name}, 
        Age: {self.age}, 
        Gender: {self.__gender}, 
        Phone: {self.__phone}, 
        Address: {self.__address}
"""