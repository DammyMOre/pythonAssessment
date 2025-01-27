class Address:
    def __init__(self, house_number,street, city, state):
        self.__house_number = house_number
        self.__street = street
        self.__city = city
        self.__state = state

    def __str__(self):
        return f'{self.__house_number} {self.__street} {self.__city} {self.__state}'
