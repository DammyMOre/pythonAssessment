class Appointment:
    def _init_(self, patient_id, doctor_name, appointment_date, appointment_time, purpose):
        self.patient_id = patient_id
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.purpose = purpose

    def _str_(self):
        return (
            f"Appointment Details:\n"
            f"  Patient ID: {self.patient_id}\n"
            f"  Doctor's Name: {self.doctor_name}\n"
            f"  Date: {self.appointment_date}\n"
            f"  Time: {self.appointment_time}\n"
            f"  Purpose: {self.purpose}"
        )


if _name_ == "_main_":
    appointment = Appointment(
        patient_id="P12345",
        doctor_name="Dr. Alice Smith",
        appointment_date="2025-01-22",
        appointment_time="10:00",
        purpose="Routine Checkup"
    )
    print(appointment)