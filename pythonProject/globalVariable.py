
import reflex as rx

loggedIn = False


current_username = ""
class TrackState(rx.State):
    habits: list[str] = []
    #username: str = ""  # Populate this on login

    async def load_habits(self):
        from pythonProject.models import habit
        with rx.session() as session:
            results = session.query(habit).filter_by(username=current_username).all()
            self.habits = [habit.habit_Name for habit in results]
