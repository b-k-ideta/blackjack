
class Trump:

    def __init__(self, suits, number):
        self.__suits = suits
        self.__number = number

    @property
    def suits(self):
        return self.__suits
    
    @property
    def number(self):
        return self.__number

        