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



def calendarHeader(year, month):
    print(month)
    print(type(month))
    monthText = calendar.month_name[month]
    return rx.box(
        rx.hstack(
            rx.icon_button("arrow-left", bg="lightblue"),
            rx.heading(
                f"{rx.cond(State.current_month == 1, "January",
                    rx.cond(State.current_month == 2, "February",
                    rx.cond(State.current_month == 3, "March",
                    rx.cond(State.current_month == 4, "April",
                    rx.cond(State.current_month == 5, "May",
                    rx.cond(State.current_month == 6, "June",
                    rx.cond(State.current_month == 7, "July",
                    rx.cond(State.current_month == 8, "August",
                    rx.cond(State.current_month == 9, "September",
                    rx.cond(State.current_month == 10, "October",
                    rx.cond(State.current_month == 11, "November",
                             "December")))))))))))}, {year}",
                size="3",
                margin_top="1%"),
            rx.icon_button("arrow-right", bg="lightblue"),
            margin_left="35%",
            margin_bottom="3%",
        ),
        width="100%",
    )



def get_days_of_month(year: int, month: int):
    _, num_days = calendar.monthrange(year, month)

    return [date(year, month, day) for day in range(1, num_days + 1)]



class currentDate():
    month = datetime.today().month
    year = datetime.today().year
    #def next_month(self):



def calendar_view(log_data: dict, year: int, month: int) -> rx.Component:
    days = get_days_of_month(year, month)

    return rx.box(
        calendarHeader(year, month),
        rx.grid(
            *[
                rx.box(
                    rx.text(str(day.day)),
                    bg=rx.cond(
                        log_data[day.strftime("%Y-%m-%d")],
                        "green",
                        "#141414",
                    ),
                    color="white",
                    p="2",
                    height="40px",
                    width="60px",
                    padding="5px",
                    padding_top="7px",
                    text_align="center",
                    border_radius="10px",
                    key=day.strftime("%Y-%m-%d"),
                )
                for day in days
            ],

            columns="7",
            spacing="3",
            width="100%",
            padding="10px",
        )
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
                rx.alert_dialog.title(f"Analysis for {State.habit_name}", margin_botton="10%"),
                calendar_view(State.log_data, currentDate.year, currentDate.month),
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