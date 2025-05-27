import reflex as rx
from pythonProject import authCards
from pythonProject import navBars
from pythonProject import animations
from pythonProject import habitCards
from dotenv import load_dotenv
load_dotenv()

from pythonProject.debug_state import DebugState  # or from your state module

import os
import reflex as rx

class State(rx.State):
    @classmethod
    def get_db_url(self):
        import os
        return os.getenv("DATABASE_URL") or "None"

def debug_page():
    db_url = State.get_db_url()  # get string once here
    return rx.box(
        rx.heading("Database URL at runtime:"),
        rx.text(db_url),  # pass string here
        padding="2rem",
        border="1px solid gray",
        border_radius="md",
        max_width="600px",
        margin="2rem auto"
    )


# Register your existing states here, plus add DebugState:
#
# class State(rx.State):
#     pass

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

#Authenication pages
def signUp() -> rx.Component:
    return rx.box(
        navBars.navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.signUpCard()
    )
#time to record a vid

def signIn() -> rx.Component:
    return rx.box(
        navBars.navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.loginCard(),
        align="center",
        width="100%",
    )




def dashboard() -> rx.Component:
    return rx.box(
        navBars.viewsNavbar(),
        rx.color_mode.button(position="bottom-left"),
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


    )

def add() -> rx.Component:
    return rx.box(
        navBars.viewsNavbar(),
        rx.color_mode.button(position="bottom-left"),
        habitCards.addCard(),
    )

def track() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="bottom-left"),
        navBars.viewsNavbar(),
        habitCards.trackCard(),
    )


app = rx.App()


#my program pages
app.add_page(index)
app.add_page(add, route="/add")
app.add_page(track, route="/track")
app.add_page(dashboard, route="/dashboard")
app.add_page(signUp, route="/signUp")
app.add_page(signIn, route="/login")

#app.add_state(DebugState)

# Register your existing pages here, plus add debug_page:
app.add_page(debug_page, route="/debug")
