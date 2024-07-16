class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 30)
h2 = House("ЖК Пётр Великий", 2)
h1.__str__()
h2.__str__()
h1.__len__()
h2.__len__()
