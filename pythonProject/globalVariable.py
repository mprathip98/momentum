
import reflex as rx

loggedIn = False


current_username = ""
class TrackState(rx.State):
    habits: list[str] = []
    #username: str = ""  # Populate this on login

    async def load_habits(self):
        from pythonProject.models import Habit
        with rx.session() as session:
            results = session.query(Habit).filter_by(username=current_username).all()
            self.habits = [habit.habit_Name for habit in results]

class dashboard(rx.State):
    habit: list[str] = []
    #username: str = ""  # Populate this on login

    async def load_habits2(self):
        from pythonProject.models import Habit
        with rx.session() as session:
            results = session.query(Habit).filter_by(username=current_username).all()
            self.habit = [habit.habit_Name for habit in results]
        print(self.habit)

def load():
    print(dashboard.habit)
    for items in rx.foreach(dashboard.habit):
        return rx.card(
            rx.link(
                rx.text(items, size="5", weight="bold", text_align="center", width="100%", margin_bottom="5%",
                        color=rx.color_mode_cond(light="black", dark="white")),

            ),
            class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
            margin="5%",
            width="20%",
            align="center",
            align_center="center",
        )


