from pythonAssessment.medicalproject.user import User


class Patient(User):
    def __init__(self,name, age, gender, phoneNumber,house_number,street, city, state,patient_id ):
        super().__init__(name, age, gender, phoneNumber,house_number,street, city, state)
        self.patient_id =patient_id


        def __str__(self):
            return f"""
            {super().__str__()}
            Patient ID: {self.__patient_id}
            """


        def get_patient_name(self):
            return f"""
            Patient Name: {self.name}
            Patient ID: {self.__patient_id}
            """


