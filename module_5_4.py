class House:
    houses_history = []  # Атрибут класса для хранения истории

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        house_name = args[0]  # Название берется из первого элемента args
        cls.houses_history.append(house_name)
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        # Выводим сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h1  # ЖК Эльбрус снесён, но он останется в истории