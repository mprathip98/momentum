import reflex as rx
from pythonProject import globalVariable
from pythonProject import models

class State(rx.State):
    habit_name: str = ""


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

def analysis(habit):
    pass
    # with rx.session() as session:
    #     habits = session.query(models.habitLog).filter_by(habit_Name=habit, username=globalVariable.current_username).all()


def eachCard(habit: dict):
    parts = habit.split("-")
    habit_name = rx.cond(
        parts.length() > 0, parts[0], ""
    )
    description = rx.cond(parts.length() > 1, parts[1], "")



    return rx.card(
        rx.text(
            habit_name,
            size = "5",
            weight = "bold",
            text_align = "center",
            width = "100%",
            color = rx.color_mode_cond(light="black", dark="white"),
            white_space  = "-",
            margin_bottom="5%",
        ),

        rx.text(description, margin_top = "2%", margin_bottom = "5%"),
        # i am trying to access the database with
        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button(
                    "Click to Analyze",
                    margin_top = "25%",
                    border_radius = "5px",
                ),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title(f"Analysis for {habit_name}"),
                rx.alert_dialog.description(analysis(habit_name)),
            ),
        ),


        class_name="rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        margin="5%",
        width="20%",
        align="center",
        text_align="center",
        padding="3%",
    )