import reflex as rx
from pythonProject import globalVariable
from pythonProject import models

class HabitState(rx.State):
    loaded = False
    habits: list[str] = []
    habitsText = "Your habits are: "

    def load_habits(self):
        self.loaded = True
        with rx.session() as session:
            self.habits = []
            self.habitsText = "Your habits are: "
            results = session.query(models.Habit).filter_by(username=globalVariable.current_username).all()
            self.habits = [habit.habit_Name for habit in results]
            for items in self.habits:
                self.habitsText += "\n" + items + ","
