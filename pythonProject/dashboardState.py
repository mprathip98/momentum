import reflex as rx
from pythonProject import globalVariable
from pythonProject import models

class HabitState(rx.State):
    loaded = False
    habits: list[str] = []

    def load_habits(self):
        self.loaded = True
        with rx.session() as session:
            self.habits = []
            results = session.query(models.habit).filter_by(username=globalVariable.current_username).all()
            for items in results:
                combinedText = f"{items.habit_Name} - {items.description}"
                self.habits.append(combinedText)
