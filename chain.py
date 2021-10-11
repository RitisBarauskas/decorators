import datetime


handlers = []


def doc_handler(func):
    handlers.append(func)
    return func


class Human:
    def __init__(self, name, age, appendicitis, covid):
        self.name = name
        self.age = age
        self.appendicitis = appendicitis
        self.covid = covid


@doc_handler
def handle_age(human):
    if human.age % 3 == 0:
        print(f'{human.name}, тебе пора пройти диспансеризацию')


@doc_handler
def handle_append(human):
    if human.appendicitis:
        print(f'{human.name}, не хочешь ли вырезать у себя лишнее?')


@doc_handler
def handle_covid(human):
    now = datetime.date.today()
    if (now - human.covid) > datetime.timedelta(days=180):
        print(f'{human.name}, тебе поставили прививку от COVID-19')
        human.covid = now
    else:
        print(f'{human.name}, тебе рано ставить прививку от COVID-19')


class Hospital:
    def __init__(self, handlers=None):
        self.handlers = handlers or []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_doc(self, human):
        for handler in self.handlers:
            handler(human)


if __name__ == '__main__':
    hospital = Hospital(handlers)
    alex = Human(
        'Alex',
        33,
        True,
        datetime.date(2021, 7, 31),
    )

    bob = Human(
        'Bob',
        35,
        False,
        datetime.date(2021, 1, 31),
    )

    hospital.handle_doc(alex)
    hospital.handle_doc(bob)
