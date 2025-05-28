import reflex as rx
from pythonProject import globalVariable
from pythonProject import models


class HabitState(rx.State):
    habits: list[str] = []

    def load_habits(self):
        with rx.session() as session:
            self.habits = session.query(models.Habit).filter_by(username=globalVariable.current_username).all()
