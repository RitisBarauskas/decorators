from __future__ import annotations
from abc import abstractmethod


class Creator:
    """
    Создатель
    """

    @abstractmethod
    def creator_method(self):
        pass

    def creator_operation(self):
        car = self.creator_method()
        return f"{car.operation()}. Это сделал создатель."


class FirstFactory(Creator):
    """
    Фабрика по производству автомобилей ВАЗ
    """

    def creator_method(self) -> Car:
        return LadaCar()


class SecondFactory(Creator):
    """
    Фабрика по производству автомобилей BMW
    """
    def creator_method(self) -> Car:
        return BMWCar()


class Car:
    """
    Автомобиль
    """

    @abstractmethod
    def operation(self):
        pass


class LadaCar(Car):
    def operation(self):
        return "Только что родилась новая Лада"


class BMWCar(Car):
    def operation(self):
        return "Выпущен новый автомобиль BMW"


def print_custom(creator: Creator):
    print(f"{creator.creator_operation()}", end="")


if __name__ == "__main__":
    print("Обращаемся к методу класса BMWCar напрямую:")
    print(BMWCar().operation())
    print("Обращаемся к методу класса BMWCar через создателя:")
    print_custom(SecondFactory())
    print("\n")

    print("Обращаемся к методу класса LadaCar напрямую:")
    print(LadaCar().operation())
    print("Обращаемся к методу класса LadaCar через создателя:")
    print_custom(FirstFactory())
    print("\n")
