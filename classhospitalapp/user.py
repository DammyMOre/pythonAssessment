import datetime


class User:
    def __init__(self, first_name, last_name, phone_number, gender, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender
        self.date_of_birth = date_of_birth
        
    @property
    def __phone_number(self):
        return self._phone_number
    
    @__phone.setter
    def __phone(self, value):
        if len(value) != 11:
            raise ValueError('Phone number must be 11 digits')
        self._phone_number = value
        
    def get_phone_number(self):
        return self.__phone_number
    
    
    
    def __calculate_age(self):
        day,month,year = self.date_of_birth.split('-')
        current_year = datetime.datetime.now().year
        if int(year) > current_year:
            raise ValueError('invalid date of birth')
        return int(current_year) - int(year) 
    
    def __str__(self):
        return (f"name: {self.first_name} {self.last_name}phone number: {self.phone_number}"
                f'gender: {self.gender}'
                f'age: {self.__calculate_age()}')
    
    user = ("emmanuel","oluwaseun","p")
                
        
        
        