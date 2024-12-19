from person import Person

class Employee(Person):
    def __init__(self, name, age,dob,gender,phoneNumber,number,street,city,state,id,level,email):
        super().__init__(name, age,dob,gender,phoneNumber,street,city,state)
        self.__id = id
        self.__level = level
        self.__email = email

        def __str__(self):
            return f"""
            {super().__str__()}
            Employee ID: {self.__id}
            Employee Email: {self.__email}
            Employee Level: {self.__level}
            """

        #s1 = Employee("dammy", 24,"18-10-2000","f","80665553344","23","sabo","yaba","Lagos","mcs0012","senior","dammy@gmail.com")
        #print(s1)
