class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.color = list(color)
        self.filled = False
        self.sides = [1] * self.sides_count  # Задать стороны по умолчанию
        if self._is_valid_sides(*sides):
            self.set_sides(*sides)

    def get_color(self):
        return self.color

    def _is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(x, (int, float)) and x > 0 for x in new_sides)

    def get_sides(self):
        return self.sides

    def len(self):
        return sum(self.sides)  # Возвращает периметр для 2D фигур

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.radius = self.get_sides()[0]  # Рассчитываем радиус по длине окружности

    def get_square(self):
        return 3.14159 * (self.radius ** 2)  # Площадь круга

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.sides = [new_sides[0]]  # В круге только одна сторона
            self.radius = new_sides[0]  # Обновляем радиус


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5  # Площадь треугольника по формуле Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.sides = [new_sides[0]] * self.sides_count  # Все 12 рёбер равны
        else:
            self.sides = [1] * self.sides_count  # По умолчанию

    def get_volume(self):
        return self.sides[0] ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Ожидаемый вывод: [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Ожидаемый вывод: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(6)  # Теперь правильно изменяем стороны куба
print(cube1.get_sides())  # Ожидаемый вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Ожидаемый вывод: [15]

# Проверка периметра (круга), это и есть длина:
print(circle1.len())  # Ожидаемый вывод: 15 (периметр)

# Проверка объёма (куба):
print(cube1.get_volume())  # Ожидаемый вывод: 216 (объём)