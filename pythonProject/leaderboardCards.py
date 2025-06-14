import reflex as rx
from pythonProject import leaderboardState
from pythonProject import models

class monthState(rx.State):
    @rx.var
    def retrieve(self) -> str:
        logs = {}
        text = ""

        with rx.session() as session:
            users = session.query(models.usersignupmodel1).all()

            for user in users:
                count = session.query(models.habitlog).filter_by(username=user.username).count()
                logs[user.username] = count
            print(logs)
            for k,v in logs.items():
                text += f"{k} -> {v}\n"

        print(text)
        return text

def mainCard():
    return rx.card(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Month", value = "month"),
                rx.tabs.trigger("Year", value = "year"),
                rx.tabs.trigger("Lifetime", value = "lifetime"),
            ),
            rx.tabs.content(
                value="month"
            ),

            rx.tabs.content(
                value="year"
            ),
            rx.tabs.content(
                rx.text(monthState.retrieve),
                value="lifetime"
            )

        ),
        align="center",
        align_items="center",
        width = "75%",
        margin = "3%",
        margin_left = "12%",
    )