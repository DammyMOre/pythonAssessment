from datetime import datetime

from pythonAssessment.medicalproject.hospitalpage import main_menu
from pythonAssessment.medicalproject.user import User

class Doctors(User):
    def __init__(self, name,age,gender,phoneNumber,house_number,street, city, state,specialization ):
        super().__init__(name,age,gender,phoneNumber,house_number,street,city, state)
        self.__doctor_id = f"DOC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.__specialization = specialization


    def __str__(self):
        return f"""
            {super().__str__()}
            Doctor iD: {self.__doctor_id}
            Specialization: {self.__specialization}
            """

    def get_doctors_name(self):
        return f"""
        Doctors Name: {self.name}
        Doctor iD: {self.__doctor_id}
        Specialization: {self.__specialization}
        
        """
if __name__ == "__main__":
    doctor = Doctors("titi",13,"f",
                     "09088776655","23",
                     "marcurley","yaba","ogun","Radiology")
                    doctor.get_doctors_name()
