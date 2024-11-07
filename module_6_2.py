class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Атрибут класса с допустимыми цветами

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner  # Атрибут владельца
        self.__model = model  # Скрытый атрибут модели
        self.__engine_power = engine_power  # Скрытый атрибут мощности двигателя
        self.__color = color if color.lower() in [c.lower() for c in self.__COLOR_VARIANTS] else self.__COLOR_VARIANTS[0]  # Скрытый атрибут цвета, по умолчанию первый цвет

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in [c.lower() for c in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Атрибут класса с ограничением на количество пассажиров

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)  # Вызов конструктора родительского класса


# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()