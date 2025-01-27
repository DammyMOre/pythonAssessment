from pythonAssessment.HospitalApplication.user import User


class Doctor(User):
    def _init_(self, doctor_id, specialization, name, age, number, street, city, state, gender, phone):
        super()._init_(name, age, number, street, city, state, gender, phone)
        self.__doctor_id = doctor_id
        self.__specialization = specialization

    def doctor_id(self):
        return self.__doctor_id


    def specialization(self):
        return self.__specialization

    def _str_(self):
        return f"""
        Doctor ID: {self.__doctor_id}
        Name: {self.get_name()}
        Specialization: {self.__specialization}
        Age: {self.get_age()}
        Gender: {self.get_gender()}
        Phone: {self.get_phone()}
        Address: {self.get_address()}
        """

if __name__ == "__main__":
    doctor = Doctor(
        doctor_id="D12345",
        specialization="Cardiology",
        name="Dr. Alice Smith",
        age=45,
        number="101",
        street="Elm Street",
        city="Springfield",
        state="IL",
        gender="Female",
        phone="987-654-3210"
    )
 print(doctor)