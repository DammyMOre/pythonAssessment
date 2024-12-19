from pythonAssessment.estore.user import User


class Customer(User):
    def __init__(self, age, email, address, name, password, phoneNumber, billingInfo, shippingCart):
        super().__init__(age,email,address,name,password,phoneNumber)
        self.billingInfo = billingInfo
        self.shippingCart = shippingCart
