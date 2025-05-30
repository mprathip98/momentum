import reflex as rx
from numpy._core.defchararray import strip
from pygments.lexer import combined

from pythonProject import globalVariable
from pythonProject import models
from reflex.vars import Var


import calendar
from datetime import datetime, date


def get_days_of_month(year: int, month: int):
    _, num_days = calendar.monthrange(year, month)
    return [date(year, month, day) for day in range(1, num_days + 1)]

def calendar_view(log_data: dict, year: int, month: int) -> rx.Component:
    days = get_days_of_month(year, month)


    return rx.grid(
        *[
            rx.box(
                rx.text(str(day.day)),
                bg=rx.cond(
                    (day_key := day.strftime("%Y-%m-%d")) & log_data.get(day_key, False),
                    "green",
                    "gray",
                ),
                p="2",
                border_radius="15px",
                text_align="center",
                key=day.strftime("%Y-%m-%d"),
            )
            for day in days
        ],
        columns="7",
        spacing="2",
        width="100%",
    )
#OMG use the reference to help me write my code. remember i told you that the color is not showing for the day. green if that day is true and red if that day is false and gray for all of the other days

class State(rx.State):
    habit_name: str = ""
    analysis_result = {}
    refresh_counter: int = 0

    @rx.var
    def has_habits(self) -> bool:
        return self.habit_name != ""

    @rx.event
    def set_habit_name(self, name: str):
        self.habit_name = name

    def analyze(self):
        habit_logs: dict = {}
        with rx.session() as session:
            habits = session.query(models.habitlog).filter_by(habit_Name = strip(self.habit_name), username = globalVariable.current_username).all()
        for item in habits:
            # Convert string to date if needed
            if isinstance(item.date, str):
                date_obj = datetime.strptime(item.date, "%Y-%m-%d").date()
            else:
                date_obj = item.date

            habit_logs[date_obj.strftime("%Y-%m-%d")] = item.status

        self.analysis_result = habit_logs

    @rx.var
    def log_data(self) -> dict:
        return self.analysis_result


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
                    margin_left = "20%",
                    height="40px",
                    weight = "bold",
                    on_click=State.analyze,
                ),
            ),

            rx.alert_dialog.content(
                rx.alert_dialog.title(f"Analysis for {State.habit_name}"),
                rx.alert_dialog.description(State.analysis_result),
                rx.text(f"Refresh count: {State.refresh_counter}"),
                calendar_view(State.log_data, 2025, 5),

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