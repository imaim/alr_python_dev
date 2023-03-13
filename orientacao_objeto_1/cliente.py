class Cliente:

    def __init__(self, nome):
        self.__name = nome

    @property
    def name(self):
        print("chamando @property nome()")
        return self .__name.title()

    @name.setter
    def name(self, nome):
        print("chamando setter nome()")
        self.__name = nome
