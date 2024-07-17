class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if not isinstance(other.number_of_floors, int):
            raise TypeError('Число этажей должно быть целым')
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value



h1 = House('ЖК Эльбрус', 30)
h2 = House("ЖК Пётр Великий", 2)


print(h1)
print(h2)

print(h1==h2)

h2.number_of_floors=h2.number_of_floors+10
print(h2)
print(h2==h1)

h2.number_of_floors+=10
print(h2)

h1.number_of_floors=10+h1.number_of_floors
print(h1)

print(h1>h2)
print(h1>=h2)
print(h1<h2)
print((h1<=h2))
print(h1!=h2)




