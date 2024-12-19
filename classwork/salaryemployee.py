from employee import Employee


class SalaryEmployee(Employee):

    def _init_(self, salary, id, level, email, name,  age, number, street, city, state, dob, gender, phone):
      super()._init_(id, level, email, name,  age, number, street, city, state, dob, gender, phone)
      self.__salary = salary
    def _str_(self):
        return f"""
            {super()._str_()}
            Salary: {self.__salary}
            """

s1 = SalaryEmployee("100000", 2423, "senior", "k-cash@gmail", "chigbo", 25,312, "ikoyi", "ikeja", "Lagos", "10/25/99", "male", "0906578")
print(s1)