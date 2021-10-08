class BaseClass:
    """
    Базовый класс.
    """

    def make(self):
        pass


class Human(BaseClass):
    """
    Основной компонент - "Человек", которого будет "одевать" при помощи декораторов
    """

    def make(self):
        return "Человек"


class Decorator(BaseClass):
    """
    Базовый класс декоратора
    """

    _human: Human = None

    def __init__(self, human: Human):
        self._human = human

    @property
    def human(self):
        """
        При помощи декоратора получаем нового "обёрнутого" человека.
        Дальше уже работаем с ним.
        """

        return self._human

    def make(self):
        return self._human.make()


class ShoesDecorator(Decorator):
    """
    Декоратор "надевает" ботинки
    """

    def make(self):
        return f"{self.human.make()} в ботинках"


class SuitDecorator(Decorator):
    """
    Декоратор "надевает" костюм
    """

    def make(self):
        return f"{self.human.make()} надел костюм"


def print_custom(human: Human):
    print(f"Сейчас есть: {human.make()}", end="\n")


if __name__ == "__main__":
    alex = Human()
    print('Алекс пришел в магазин')
    print_custom(alex)
    print('Надеваем Алексу ботинки')
    shoes = ShoesDecorator(alex)
    print_custom(shoes)
    print('Надеваем Алеку костюм')
    suit = SuitDecorator(alex)
    print_custom(suit)
    print('Надеваем Алексу в ботинках костюм')
    suit_and_shoes = SuitDecorator(shoes)
    print_custom(suit_and_shoes)
    print('Но иногда примерка выходила из под контроля и получалось что-то такое:')
    mix_alex = ShoesDecorator(SuitDecorator(suit_and_shoes))
    print_custom(mix_alex)
