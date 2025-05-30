import reflex as rx
from pythonProject import globalVariable
from pythonProject import models

class State(rx.State):
    habit_name: str = ""
    analysis_result: str = ""

    @rx.var
    def has_habits(self) -> bool:
        return self.habit_name != ""

    @rx.event
    def set_habit_name(self, name: str):
        self.habit_name = name

    def analyze(self):
        with rx.session() as session:
            habits = session.query(models.habitlog).filter_by(
                habit_Name=self.habit_name,
                username=globalVariable.current_username
            ).all()
        print(habits)
        self.analysis_result = str(habits)

def eachCard(habit):
    parts = habit.split("-")
    name = rx.cond(parts.length() > 0, parts[0], "")
    description = rx.cond(parts.length() > 1, parts[1], "")

    return rx.card(
        rx.text(
            name,
            size = "5",
            weight = "bold",
            text_align = "center",
            width = "100%",
            color = rx.color_mode_cond(light="black", dark="white"),
            margin_bottom="5%",
        ),
        rx.text(description, margin_top = "2%", margin_bottom = "5%"),

        #on_click=rx.call(State.set_habit_name, name),

        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button(
                    "Click to Analyze",
                    margin_top = "25%",
                    border_radius = "5px",
                    on_click=State.analyze,
                ),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title(f"Analysis for {State.habit_name}"),
                rx.alert_dialog.description(State.analysis_result),
            ),
        ),
        on_click=lambda: State.set_habit_name(name),
        class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        margin="5%",
        width="20%",
        align="center",
        text_align="center",
        padding="3%",
    )





def addCard():
    return rx.card(
        rx.link(
            rx.color_mode_cond(
                light=rx.image(
                    src="/darkPlus.png",
                    width="50%",
                    margin_top="13%",
                    margin_bottom="10%",
                    margin_left="25%"

                ),
                dark=rx.image(
                    src="/lightPlus.png",
                    width="50%",
                    margin_top="13%",
                    margin_bottom="10%",
                    margin_left="25%"
                )

            ),
            rx.text("Add Habits", size="5", weight="bold", text_align="center", width="100%", margin_bottom="5%",
                    color=rx.color_mode_cond(light="black", dark="white")),

            href="/add"

        ),
        class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        margin="5%",
        width="20%",
        align="center",
        align_center="center",
    ),