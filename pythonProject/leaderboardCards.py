from sqlite3 import Date

import reflex as rx
from numpy import extract

from pythonProject import leaderboardState
from pythonProject import models
import datetime
from sqlalchemy import cast, extract
from sqlalchemy.types import Date


class lifetimeState(rx.State):
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

class yearState(rx.State):
    @rx.var
    def retrieveyear(self) -> dict:
        yearlogs = {}
        with rx.session() as session:
            users = session.query(models.usersignupmodel1).all()
            current_year = datetime.datetime.today().year
            for user in users:
                yearCount = session.query(models.habitlog).filter(
                    models.habitlog.username == user.username,
                    extract("year", cast(models.habitlog.date, Date)) == current_year
                ).count()
                yearlogs[user.username] = yearCount
            finalYearLogs = {k: v for k, v in sorted(yearlogs.items(), key=lambda item: item[1], reverse=True)}

            #adding color to the first three places
            first_key = list(finalYearLogs.keys())[0]
            finalYearLogs[first_key + "🥇"] = finalYearLogs.pop(first_key)

            second_key = list(finalYearLogs.keys())[1]
            finalYearLogs[second_key + ""] = finalYearLogs.pop(second_key)

            third_key = list(finalYearLogs.keys())[2]
            finalYearLogs[third_key + ""] = finalYearLogs.pop(third_key)

        return finalYearLogs

class monthState(rx.State):
    @rx.var
    def retrieveMonth(self) -> dict:
        monthLogs = {}
        with rx.session() as session:
            users = session.query(models.usersignupmodel1).all()
            current_month = datetime.datetime.today().month
            for user in users:
                monthCount = session.query(models.habitlog).filter(
                    models.habitlog.username == user.username,
                    extract("month", cast(models.habitlog.date, Date)) == current_month
                ).count()
                monthLogs[user.username] = monthCount
            finalMonthLogs = {k: v for k, v in sorted(monthLogs.items(), key=lambda item: item[1], reverse=True)}
        print(type(finalMonthLogs))
        return finalMonthLogs




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
                rx.text("YEARLY LEADERBOARD", weight="bold", size="4", width="100%", text_align="center",
                        margin_top="2%"),
                rx.hstack(
                    rx.card("username", margin_left="5%", margin_top="2%"),
                    rx.card("# of logs", margin_left="62%", margin_top="2%"),
                ),
                rx.foreach(monthState.retrieveMonth, render_habit),
                value="month"
            ),

            rx.tabs.content(
                rx.text("MONTLY LEADERBOARD", weight="bold", size="4", width="100%", text_align="center",
                        margin_top="2%"),
                rx.hstack(
                    rx.card("username", margin_left="5%", margin_top="2%"),
                    rx.card("# of logs", margin_left="62%", margin_top="2%"),
                ),
                rx.foreach(yearState.retrieveyear, render_habit),
                value="year"
            ),

            rx.tabs.content(
                rx.text("LIFETIME LEADERBOARD", weight="bold", size="4", width="100%", text_align="center", margin_top="2%"),
                rx.hstack(
                    rx.card("username", margin_left="5%", margin_top="2%"),
                    rx.card("# of logs", margin_left="62%", margin_top="2%"),
                ),
                rx.foreach(lifetimeState.retrieve, render_habit),
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