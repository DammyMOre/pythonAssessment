from pythonAssessment.HospitalApplication.user import User


class Patient(User):
    def _init_(self, patient_id, name, age, number, street, city, state, gender, phone):
        super()._init_(name, age, number, street, city, state, gender, phone)
        self.__patient_id = patient_id

    def patient_id(self) -> str:
        return self.__patient_id

    def _str_(self) -> str:
        return f"""
        Patient ID: {self.__patient_id},
        {super()._str_()}
        """

if __name__ == "__main__":
    patient = Patient(
        patient_id="P12345",
        name="John Doe",
        age=30,
        number="123",
        street="Main St",
        city="Metropolis",
        state="NY",
        gender="Male",
        phone="123-456-7890"
    )

  print(patient)