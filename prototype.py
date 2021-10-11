class ShoppingCart:

    """
    Класс - прототип
    """
    def __init__(self):
        self._obj = {}

    def add_dict(self, title, item):
        self._obj[title] = item

    def remove_dict(self, title, item):
        self._obj.pop(title, item)

    def print_dict(self):
        print(self._obj)

    def __repr__(self):
        return f'{self._obj}'


class FruitsCart:
    def __init__(self):
        self.a = 'banana'
        self.b = 'orange'
        self.c = 'eggs'

    def __repr__(self):
        return f'{self.c}, {self.b}, {self.a}'


if __name__ == "__main__":
    print('Создаем корзину покупок')
    cart = FruitsCart()
    print('Создаем список покупок, куда добавляем')
    prototype = ShoppingCart()
    prototype.add_dict('надо купить', cart)
    prototype.print_dict()
    prototype.add_dict('уже куплено', cart)
    prototype.print_dict()
    prototype.remove_dict('надо купить', cart)
    prototype.print_dict()
