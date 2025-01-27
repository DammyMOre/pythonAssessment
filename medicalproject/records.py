from pythonAssessment.medicalproject.user import User


class Records:
    def __init__(self):
        self.booked_appointments = []
        self.registered_doctors = []
        self.registered_patients = []
        self.counter = 0
    #def book_appointment(self):


    def register_doctor(self, doctor):
        self.registered_doctors.append(doctor) if doctor not in self.registered_doctors else "Name already exist"
        self.counter += 1


    def register_patient(self,patient):
        if patient not in self.registered_patients:
            self.registered_patients.append(patient)
        else:"Name already exist"
        self.counter += 1

    def book_appointment(self,doctor,patient,date):
        ...









