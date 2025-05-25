import reflex as rx
import asyncio
import reflex_local_auth
from rxconfig import config
from pythonProject import databaseTables
from pythonProject import authStates
from pythonProject import authCards
from pythonProject import navBars
signInState1 = authStates.signInState

class State(rx.State):
    pass

#-----Spline Setup----------
class Spline(rx.Component):
    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]
spline = Spline.create
#link for the animation on Spline
scene = "https://prod.spline.design/WgCVJEkCUF1CFaaP/scene.splinecode"

#------------HOME PAGE----------------
def index() -> rx.Component:
    return rx.box(
        navBars.navbar(),

        rx.color_mode.button(position="bottom-left"),
        rx.hstack(
            #rx.heading("*blank space for the animation*"),
            rx.box(
                spline(scene=scene),
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
        navBars.dashboardNavbar(),

        # rx.cond(
        #     authStates.State.user_info.get("username") != "",
        #     rx.text("No user logged in")
        # )
    )





#pages initialization
app = rx.App()

#reflex local auth pages
app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
#my program pages
app.add_page(index)
app.add_page(dashboard, route="/dashboard")
app.add_page(signUp, route="/signUp")
app.add_page(signIn, route="/login")
