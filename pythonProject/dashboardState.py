import reflex as rx
from pythonProject import globalVariable
from pythonProject import models

class HabitState(rx.State):
    loaded = False
    habits: list[str] = []
    descriptions: list[str] = []

    def load_habits(self):
        self.loaded = True
        with rx.session() as session:
            self.habits = []
            results = session.query(models.Habit).filter_by(username=globalVariable.current_username).all()
            self.habits = [habit.habit_Name + "\n - " + habit.description for habit in results]
            #self.descriptions = [habit.habit_Name for habit in results]

#