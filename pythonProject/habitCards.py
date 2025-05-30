import reflex as rx
from pythonProject import globalVariable
from pythonProject import models
from pythonProject import habitState

from pythonProject import habitState

class State(rx.State):
    local_username: str = ""

def addCard():
    return rx.card(
        rx.center(
            rx.form(
                rx.vstack(
                    rx.color_mode_cond(
                        dark=rx.image(
                            src="/momentumLogo.png",
                            alt="Reflex Logo light",
                            height="4em",
                            ),

                        light=rx.image(
                            src="/momentumLogoBlack.png",
                            alt="Reflex Logo dark",
                            height="4em",
                            ),
                    ),

                    rx.heading("Add a new habit", size="5"),

                    rx.vstack(
                        rx.text(
                            "habit name",
                            size="4",
                            text_align="left",
                            weight="medium",
                            width="100%"
                        ),
                        rx.input(
                            name="habit_Name",
                            required=True,
                            placeholder="workout for two hours",
                            type="text",
                            width="300px",
                            size="3",
                            margin_top="-2%"
                        ),
                        margin="8%",
                    ),
                    rx.vstack(
                        rx.text(
                            "description",
                            size="4",
                            text_align="left",
                            weight="medium",
                            width="100%"
                        ),
                        rx.text_area(
                            type="text",
                            name="description",
                            required=True,
                            placeholder="brief description",
                            width="300px",
                            size="3",
                            margin_top="-2%"
                        ),
                        margin="1%",
                    ), #is a text_area also considered an input in python reflex's form

                    rx.button(
                        "Add",
                        width="50%",
                        size="3",
                        margin_top="6%",
                        margin_bottom="5%",
                        align="center",
                        font_weight="bold",
                        font_size="1em",
                        type="submit",
                        # on_click=errorCheck,
                    ),
                    border_color="white",
                    align="center",
                ),

                align="center",
                on_submit=habitState.AddState.handle_submit,
                reset_on_submit=True,
            ),

        ),
        width="35%",
        align="center",
        margin="2%",
        margin_left="32%",
        margin_top="5%",
        border_color="white",
        # trying to add a shadow to a card
        # how can i add a neon box shadow to a rx.card on a black card
        class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
    ),


def trackCard():

    return rx.card(

        rx.center(
            rx.form(
                rx.vstack(
                    rx.color_mode_cond(
                        dark=rx.image(
                            src="/momentumLogo.png",
                            alt="Reflex Logo light",
                            height="4em",
                            ),

                        light=rx.image(
                            src="/momentumLogoBlack.png",
                            alt="Reflex Logo dark",
                            height="4em",
                            ),
                    ),


                    rx.heading("Track your habit", size="5"),

                    rx.hstack(

                        ##left stack
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "choose a habit",
                                    size="4",
                                    text_align="left",
                                    weight="medium",
                                    width="100%",
                                    margin_bottom="-2%"

                                ),
                                rx.select(
                                    globalVariable.TrackState.habits,
                                    name="habit_Name",
                                    required=True,
                                    placeholder="select habit",
                                    width="300px",
                                    size="3",
                                ),
                                margin_bottom="4%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "when is this log for?",
                                    size="4",
                                    text_align="left",
                                    weight="medium",
                                    width="100%"
                                ),

                                rx.el.input(
                                    type="date",
                                    name="date",
                                    required=True,
                                    width="300px",
                                    class_name=" px-3 py-2 border rounded-md  sm:text-sm",
                                    margin_top="-2%",
                                ),
                                margin_top="2%",
                            ),
                            margin="5%",
                        ),


                        #right stack
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "did you crush your goal?",
                                    size="4",
                                    text_align="right",
                                    weight="medium",
                                    width="100%",
                                    margin_top="-2%"
                                ),
                                rx.select(
                                    ["crushed it", "not today"],
                                    name="status",
                                    required=True,
                                    width="300px",
                                    size="3",
                                    placeholder="select status",
                                    margin_top="-2%",
                                    border_color="white",
                                    border = "2px"
                                ),
                                margin="1%",
                            ),

                            rx.vstack(
                                rx.text(
                                    "so, how did it go?",
                                    size="4",
                                    text_align="right",
                                    weight="medium",
                                    width="100%"
                                ),
                                rx.input(
                                    type="text",
                                    required=True,
                                    placeholder="brief description",
                                    width="300px",
                                    size="3",
                                    margin_top="-2%"
                                ),
                                margin="1%",
                                margin_top="4%",
                            ),
                            margin="5%",
                        ),
                        margin_right="20%",
                    ),


                    rx.button(
                        "Log",
                        width="40%",
                        size="3",
                        margin_bottom="5%",
                        align="center",
                        font_weight="bold",
                        font_size="1em",
                        type="submit",

                    ),
                    border_color="white",
                    align="center",
                ),

                align="center",
                on_submit=habitState.habitLog.handle_submit,
                reset_on_submit=True,
            ),

        ),
        width="65%",
        align="center",
        margin="2%",
        margin_left="17.5%",
        margin_top="5%",
        border_color="white",
        class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        #on_mount=globalVariable.TrackState.load_habits,
    ),
