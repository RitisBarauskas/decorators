from abc import abstractmethod


class State:

	@abstractmethod
	def eat(self):
		pass

	@abstractmethod
	def make_money(self):
		pass

	@abstractmethod
	def dream(self):
		pass


class WorkState(State):

	def eat(self):
		return 'Можешь позволить себе час на обед'

	def make_money(self):
		return 'Каждый новый час приближает тебя к новому автомобилю'

	def dream(self):
		return 'Поспать можешь, но тогда придется пожертвовать обедом'


class WeekendState(State):

	def eat(self):
		return 'Можешь есть в любое время'

	def make_money(self):
		return 'Зарабатывать можно, но лучше не нужно. В выходные надо отдыхать.'

	def dream(self):
		return 'Если ребенок у бабушки с дедом, то можешь поспать'


class SleepState(State):

	def eat(self):
		return 'Есть во сне сложно и опасно'

	def make_money(self):
		return 'Можно открыть брокерский счет. Пусть идет пассивный доход.'

	def dream(self):
		return 'тебя Невозможно разбудить даже пушечным выстрелом'


class Human:

	def __init__(self, state: State, name) -> None:
		self._state = state
		self.name = name

	def change_state(self, state: State) -> None:
		self._state = state

	def eat(self) -> None:
		self._execute('eat')

	def make_money(self) -> None:
		self._execute('make_money')

	def dream(self) -> None:
		self._execute('dream')

	def _execute(self, operation: str) -> None:
		try:
			state = getattr(self._state, operation)
			print(f'{self.name}, {state().lower()}.')
		except AttributeError:
			print(f'Для {self.name} это что-то новенькое, надо записать.')


if __name__ == '__main__':
	on_work = WorkState()
	sleep = SleepState()
	weekend = WeekendState()
	alex = Human(on_work, 'Alex')
	alex.make_money()
	alex.eat()
	alex.dream()
	alex.change_state(sleep)
	alex.dream()
	alex.change_state(weekend)
	alex.eat()
	alex.dream()
