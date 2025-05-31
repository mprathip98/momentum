from string import whitespace

import reflex as rx
from sqlalchemy.util import preload_module

from pythonProject import authCards
from pythonProject import navBars
from pythonProject import animations
from pythonProject import habitCards
from pythonProject import globalVariable
from pythonProject import dashboardState
from pythonProject import models
from pythonProject import dashboardCards

from dotenv import load_dotenv
load_dotenv()

#------------HOME PAGE----------------
def index() -> rx.Component:
    return rx.box(
        navBars.navbar(),

        rx.color_mode.button(position="bottom-left"),
        rx.hstack(
            #rx.heading("*blank space for the animation*"),
            rx.box(
                animations.spline(scene=animations.scene),
                width="520px",
                height="500px",
                margin_top="-4%"
            ),

            rx.vstack(
                rx.heading(
                    "Track. Analyze. Improve.",
                    size="9",
                    position="center",
                    color="skyblue",
                    margin_top="12%",

                    style={
                        "position": "relative",
                        "@keyframes opacity": {
                            "0%": {"opacity": "0"},
                            "100%": {"opacity": "1"},
                        },
                        "animation": "opacity 3s",
                    },
                ),
                rx.heading(
                    "Start building good habits",
                    size="9",
                    background_image="linear-gradient(to right, #FFFFFF, #6960ff)",  # Gradient from red to green
                    background_clip="text",
                    font_weight="bold",
                    color="transparent",
                    padding_botton="20%",
                    height="70px",
                    style={
                        "position": "relative",
                        "@keyframes opacity": {
                            "0%": {"opacity": "0"},
                            "100%": {"opacity": "1"},
                        },
                        "animation": "opacity 3s",
                    },
                ),
                rx.button(
                    rx.link("Get Started", href="/signUp", color="black", underline="none"),
                            size="4",
                            color="black",
                            width="150px",
                            height="50px",
                            bg="skyblue",
                            margin_top="5%",
                            margin_left="35%",
                            border_radius="10px",
                            background_image="linear-gradient(to right, #d8d6fa, #a4b1ff)",  # Gradient from red to green
                            font_weight="bold",
                )
            ),
            padding_top="200px",
            justify="center",
            spacing="5",
        ),

        border_radius="5px",
        border_color="white",
        height="600px",

    )
#-----------end home page


#---------start Authenication pages------------------------
def signUp() -> rx.Component:
    return rx.box(
        navBars.navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.signUpCard(),
    )

def signIn() -> rx.Component:
    return rx.box(
        navBars.navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.loginCard(),
        align="center",
        width="100%",
    )
#----------------end auth pages---------------------------------------------------------


#the class is called when the page is actually visible to the
@rx.page(on_load=dashboardState.HabitState.load_habits)
def dashboard() -> rx.Component:
    return rx.box(
        navBars.viewsNavbar(),
        dashboardCards.addCard(),
        rx.color_mode.button(position="bottom-left"),
        rx.box(  # Wrap the habit cards in a grid
            rx.cond(
                dashboardState.HabitState.loaded,
                rx.grid(
                    rx.foreach(dashboardState.HabitState.habits, dashboardCards.eachCard),
                    columns="3",
                    spacing="4",
                    width="100%",
                    justify_items="center",
                ),
            ),
            width="100%",
            padding="2%",
        ),
    )

#--------------start track pages------------------------
def add() -> rx.Component:
    return rx.box(
        navBars.viewsNavbar(),
        rx.color_mode.button(position="bottom-left"),
        habitCards.addCard(),
    )

@rx.page(on_load=globalVariable.TrackState.load_habits)
def track() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="bottom-left"),
        navBars.viewsNavbar(),
        habitCards.trackCard(),
    )
#----------------end track pages-------------------------------

app = rx.App()
#my program pages
app.add_page(index, title="Home")
app.add_page(add, route="/add", title="Add Habit")
app.add_page(track, route="/track", title="Track Habit")
app.add_page(dashboard, route="/dashboard", title="Dashboard")
app.add_page(signUp, route="/signUp", title="Sign Up")
app.add_page(signIn, route="/login", title="Login")
