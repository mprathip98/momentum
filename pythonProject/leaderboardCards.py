import reflex as rx
from pythonProject import leaderboardState
from pythonProject import models


class monthState(rx.State):
    @rx.var
    def retrieve(self) -> dict:
        logs = {}

        with rx.session() as session:
            users = session.query(models.usersignupmodel1).all()

            for user in users:
                count = session.query(models.habitlog).filter_by(username=user.username).count()
                logs[user.username] = count


            finalLogs = {k: v for k, v in sorted(logs.items(), key=lambda item: item[1], reverse=True)}


        return finalLogs

def render_habit(item: dict[str, int]):
    return rx.card(
        rx.hstack(
            rx.hstack(
                rx.text(f"{item[0]}", align="left"),
                margin_left="5%",
                width = "95%"
            ),
            rx.hstack(
                rx.text(f"{item[1]}", align="right", margin_right="2%"),
                width = "30%",
                margin_right="-10%",
                align_items="right"
            ),

        ),

        margin = "1%"
    )

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
                rx.text("LIFETIME LEADERBOARD", weight="bold", size="4", width="100%", text_align="center", margin_top="2%"),
                rx.hstack(
                    rx.card("username", margin_left="5%", margin_top="2%"),
                    rx.card("# of logs", margin_left="62%", margin_top="2%"),
                ),
                rx.foreach(monthState.retrieve, render_habit),
                #rx.text(monthState.retrieve),

                value="lifetime"
            ),
            rx.text("Select a timeframe to view the leaderboard", weight="bold", size="4", margin="5%"),
        ),
        align="center",
        align_items="center",
        width = "60%",
        margin = "3%",
        margin_left = "20%",
        border_radius = "10px",
    )