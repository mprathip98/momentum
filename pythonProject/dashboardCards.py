from numpy._core.defchararray import strip
import reflex as rx
import calendar
from datetime import datetime, date
from typing import Dict, List
from pythonProject import models
from pythonProject import globalVariable
import random

class DayRenderInfo(rx.Base):
    key: str
    display_day: str

class State(rx.State):
    habit_name: str = ""
    analysis_result = {}
    current_month: int = datetime.today().month
    current_year: int = datetime.today().year
    length: int = 0
    quote: str = ""
    cite: str = ""

    @rx.event
    async def update_quote(self):
        quotes = [
            "Depending on what they are, our habits will either make us or break us. We become what we repeatedly do. \n ―Sean Covey",
            "Don't ever stop when you're tired, stop only when you're done. \n ―David Goggins",
            "Habit is a cable; we weave a thread each day, and at last we cannot break it. \n ―Horace Mann",
            "Laziness is nothing more than the habit of resting before you get tired. \n -Jules Renard",
            "Be the designer of your world and not merely the consumer of it. \n -James Clear",
            "The chains of habit are too weak to be felt until they are too strong to be broken. \n –Samuel Johnson"]
        quote = random.choice(quotes).split("\n")
        self.quote = quote[0].strip()
        self.cite = quote[1].strip()


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
        self.length = len(habits)
        self.analysis_result = habit_logs

    def randomQuote(self):
        self.randomQuote = self.quotes[random.randint(0, 5)]
        self.quote,self.cite = self.randomQuote.split("\n")

    def streakSetter(self):
        print("streak")
        streak = 0
        today = date.today()
        while self.analysis_result.get(today.strftime("%Y-%m-%d")):
            streak += 1
            today = today.replace(day=today.day - 1)
        return streak

def calendar_header():
    return rx.hstack(
        rx.icon_button(
            "arrow-left",
            on_click=State.previous_month,
            size="2"
        ),
        rx.heading(State.current_month_year_str, size="4", padding_top="5px"),
        rx.icon_button(
            "arrow-right",
            on_click=State.next_month,
            size="2",
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
                    #margin = "5%",
                    margin_left="22%",
                    border_radius = "5px",
                    margin_top="25%",
                    #
                    height="40px",
                    weight = "bold",
                    on_click=lambda: [State.set_habit_name(name), State.analyze()],
                ),
            ),

            rx.alert_dialog.content(
                rx.alert_dialog.title(f"Analysis for {State.habit_name}", margin_botton="10%"),
                rx.alert_dialog.description(f"So far, you have logged {State.length} times for this habit."),
                rx.text(f"Current Streak: {State.streakSetter}"),
                               #
                calendar_view(),
                rx.alert_dialog.cancel(
                    rx.button("Close", margin="1%", margin_left="43.5%"),
                ),
                align_items="center",
            ),
        ),
        #on_click=lambda: State.set_habit_name(name),
        class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        margin="5%",
        width="65%",
        align_items="center",
        text_align="center",
        padding="7%",


    )


def addCard():

    return rx.box(
        rx.hstack(
            rx.card(
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
                    rx.text("Add Habits", size="5", weight="bold", text_align="center", width="100%",
                            margin_bottom="5%",
                            color=rx.color_mode_cond(light="black", dark="white")),

                    href="/add"

                ),
                class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
                margin="5%",
                margin_left="7%",
                width="20%",
                align="center",
                align_center="center",

            ),
            rx.card(

                rx.heading(State.quote),
                rx.heading(State.cite, margin_top="2%", align="right", margin_bottom="-1%"),
                class_name = "rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
                margin = "5%",
                margin_right = "7%",
                align = "center",
                align_center = "center",
                width="60%",
                padding="5%"
                #
            )
        ),
        on_mount=State.update_quote,
    )



