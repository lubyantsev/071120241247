class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        added_products = []

        for product in products:
            product_str = str(product)
            if product_str not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(product_str + '\n')
                added_products.append(product_str)
            else:
                print(f'Продукт {product_str} уже есть в магазине')

        return added_products


# Пример работы программы
if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str

    s1.add(p1, p2, p3)

    print(s1.get_products())