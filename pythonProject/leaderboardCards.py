import reflex as rx
from pythonProject import leaderboardState

def mainCard():
    return rx.card(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Month", value = "month"),
                rx.tabs.trigger("Year", value = "year"),
                rx.tabs.trigger("Lifetime", value = "lifetime"),
            ),
            rx.tabs.content(
                #rx.text(f"{leaderboardState.monthState.retrieve}"),
                rx.text(leaderboardState.monthState.retrieve),
                value="month"
            ),
            rx.tabs.content(
                value="year"
            ),
            rx.tabs.content(
                value="lifetime"
            )

        ),
        align="center",
        align_items="center",
        width = "75%",
        margin = "3%",
        margin_left = "12%",
    )