from aiogram.dispatcher.filters.state import State, StatesGroup


class Goal(StatesGroup):
    name = State()
    description = State()


class Habit(StatesGroup):
    name = State()
    description = State()


class Task(StatesGroup):
    name = State()
    description = State()


class EditGoal(StatesGroup):
    name = State()
    description = State()


class EditHabit(StatesGroup):
    name = State()
    description = State()


class EditTask(StatesGroup):
    name = State()
    description = State()
