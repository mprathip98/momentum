import reflex as rx
from pygments.styles.dracula import background

from pythonProject import authCards
from pythonProject import navBars
from pythonProject import animations
from pythonProject import habitCards
from pythonProject import globalVariable
from pythonProject import dashboardState
from pythonProject import dashboardCards
from pythonProject import background
from dotenv import load_dotenv
load_dotenv()



#------------HOME PAGE----------------
def index() -> rx.Component:
    return rx.box(
        navBars.navbar(),

        rx.color_mode.button(position="bottom-left"),
        rx.hstack(
            rx.box(
                animations.spline(scene=animations.scene),
                width="520px",
                height="500px",
                #margin_top="-4%"
            ),

            rx.vstack(
                rx.heading(
                    "Track. Analyze. Improve.",
                    size="9",
                    position="center",
                    color="skyblue",
                    #margin_top="-5%",

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
                    background_image=rx.color_mode_cond(dark="linear-gradient(to right, #FFFFFF, #6960ff)", light="linear-gradient(to right, #87ceeb, #6960ff)"),
                    background_clip="text",
                    font_weight="bold",
                    color="transparent",
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
            padding_top="5%",
            justify="center",
            spacing="5",
            z_index="10",
            height="120%",
            align_items="center",
        ),

        background.backgroundSetter(),


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
        background.backgroundSetter(),
    )


def loginRedirection() -> rx.Component:
    return rx.card(
        rx.center(
            rx.vstack(
                rx.text("You are now being redirected to the login page"),
                rx.button("Continue to Login", margin_top="5%", on_click=rx.redirect("/login")),
                align="center",
            ),

        ),
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="-1",  # Behind content
            background_size="60px 60px",
            background_image="linear-gradient(hsl(0, 0%, 35%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 40%) 100%)",
            mask="radial-gradient(45% 50% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
            mask_repeat="no-repeat",
            mask_size="100% 100%",
        ),
        margin="15%",
        margin_left="30%",
        width="40%",
        class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",

    )


def signIn() -> rx.Component:
    return rx.box(
        navBars.navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.loginCard(),
        background.backgroundSetter(),
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
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="-1",  # Behind content
            background_size="60px 60px",
            background_image="linear-gradient(hsl(0, 0%, 35%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 40%) 100%)",
            mask="radial-gradient(45% 50% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
            mask_repeat="no-repeat",
            mask_size="100% 100%",
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
#all of the program pages
app.add_page(index, title="Momentum")
app.add_page(add, route="/add", title="Momentum | Add Habit")
app.add_page(track, route="/track", title="Momentum | Track Habit")
app.add_page(dashboard, route="/dashboard", title="Momentum | Dashboard")
app.add_page(signUp, route="/signUp", title="Momentum | Sign Up")
app.add_page(loginRedirection, route="/loginRedirection", title="Momentum | Login Redirection")
app.add_page(signIn, route="/login", title="Momentum | Login")
