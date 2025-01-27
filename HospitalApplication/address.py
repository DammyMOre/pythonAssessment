class Address:
    def _init_(self, number, street, city, state):
        self.number = number
        self.street = street
        self.city = city
        self.state = state

    def _str_(self):
        return f"{self.number} {self.street}, {self.city},{self.state}"