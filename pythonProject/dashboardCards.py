import reflex as rx
from numpy._core.defchararray import strip
from pygments.lexer import combined
from pythonProject import globalVariable
from pythonProject import models
from reflex.vars import Var
import calendar
from datetime import datetime, date
import reflex as rx
import calendar
from datetime import datetime, date
from typing import Dict, List
from pythonProject import models
from pythonProject import globalVariable

class DayRenderInfo(rx.Base):
    key: str
    display_day: str

class State(rx.State):
    habit_name: str = ""
    analysis_result = {}
    current_month: int = datetime.today().month
    current_year: int = datetime.today().year

    @rx.var
    def has_habits(self) -> bool:
        return self.habit_name != ""

    @rx.var
    def log_data(self) -> dict:
        return self.analysis_result

    @rx.var
    def calendar_days_list(self) -> List[DayRenderInfo]:
        days_list: List[DayRenderInfo] = []
        _, num_days = calendar.monthrange(self.current_year, self.current_month)
        for day_num in range(1, num_days + 1):
            current_date_obj = date(self.current_year, self.current_month, day_num)
            days_list.append(
                DayRenderInfo(
                    key=current_date_obj.strftime("%Y-%m-%d"),
                    display_day=str(current_date_obj.day),
                )
            )
        return days_list

    @rx.var
    def current_month_year_str(self) -> str:
        return f"{calendar.month_name[self.current_month]} {self.current_year}"

    @rx.event
    def previous_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        yield State.analyze()

    @rx.event
    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        yield State.analyze()

    @rx.event
    def set_habit_name(self, name: str):
        self.habit_name = name

    @rx.event
    def analyze(self):
        self.analysis_result = {}
        habit_logs: dict = {}
        with rx.session() as session:
            habits = session.query(models.habitlog).filter_by(
                habit_Name=strip(self.habit_name),
                username=globalVariable.current_username
            ).all()
        for item in habits:
            date_obj = item.date if not isinstance(item.date, str) else datetime.strptime(item.date, "%Y-%m-%d").date()
            habit_logs[date_obj.strftime("%Y-%m-%d")] = item.status
        self.analysis_result = habit_logs



def calendar_header():
    return rx.hstack(
        rx.icon_button(
            "arrow-left",
            on_click=State.previous_month,
            bg="lightblue",
            size="2"
        ),
        rx.heading(State.current_month_year_str, size="4"),
        rx.icon_button(
            "arrow-right",
            on_click=State.next_month,
            bg="lightblue",
            size="2"
        ),
        justify="center",
        spacing="4",
        margin_bottom="1em",
    )

def calendar_day_item(day_info: DayRenderInfo) -> rx.Component:
    return rx.box(
        rx.text(day_info.display_day),
        class_name=rx.cond(
            State.log_data.contains(day_info.key),
            rx.cond(
                State.log_data[day_info.key],
                "bg-green-500 text-white",
                "bg-red-500 text-white",
            ),
            "bg-gray text-gray-600",
        ),
        width="2em",
        height="2em",
        display="flex",
        align_items="center",
        justify_content="center",
        border_radius="10px",
    )


def calendar_view():
    return rx.vstack(
        calendar_header(),
        rx.grid(
            rx.foreach(State.calendar_days_list, calendar_day_item),
            columns="7",
            gap="2",
            spacing="2",
        ),
        align_items="center",
        padding="1em",
        border_radius="lg",
        box_shadow="md",
    )


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
                rx.alert_dialog.title(f"Analysis for {State.habit_name}", margin_botton="10%"),
                rx.alert_dialog.description(f"So far, you have logged {State.log_data} times for this habit"),
                calendar_view(),
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