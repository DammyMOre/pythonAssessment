from pythonAssessment.medicalproject.records import Records
from pythonAssessment.medicalproject.doctors import Doctors

def register_doctor():
    name = input("Enter your name: ")
    age = input("Enter your age:")
    gender = input("Enter your gender:")
    phone_number =input("Enter your phone_number:")
    house_number = input("Enter your house_number:")
    street = input("Enter your street:")
    city = input("Enter your city:")
    state = input("Enter your state:")
    specialization = input("Enter your Area of Specialization:")
    doctor = Doctors(name, age, gender, phone_number, house_number, street, city, state, specialization)
    new_record = Records()
    new_record.registered_doctors(doctor)
    print(new_record.booked_appointments)
    main_menu()


def check_appointment():
    pass


def register_patient():
    pass


def book_appointment():
    pass
def main_menu():
    menu = """
        "Welcome to Group-one Hospital"
         What will you like to do?

        1-> Register as a Doctor
        2-> Register as a Patient
        3-> check Appointment
        4-> Book Appointment
    """
    print(menu)
    user_input = int(input(""))

    match user_input:
        case 1: register_doctor()
        case 2: register_patient()
        case 3: check_appointment()
        case 4: book_appointment()


if __name__ == '__main__':
    main_menu()

