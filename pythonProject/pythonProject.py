
import reflex as rx
from reflex.components.radix.primitives.form import FormSubmit
from rich.jupyter import display
import asyncio
import reflex_local_auth
from rxconfig import config
from pythonProject import authStates
from pythonProject import authCards


class State(rx.State):
    error_call: bool = False

#----------HOME PAGE------------------
def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.color_mode_cond(
                        light=rx.image(
                            src="/momentumLogo.png",
                            alt="Reflex Logo light",
                            height="4em",
                            padding_left="30px",
                        ),
                        dark=rx.image(
                            src="/momentumLogoBlack.png",
                            alt="Reflex Logo dark",
                            height="4em",
                            padding_left="30px",
                        ),
                    ),
                ),
                rx.hstack(
                    rx.button(
                        rx.link("sign up", href="/signUp", color=rx.color_mode_cond(light="white", dark="black"), underline="none"),
                        size="3",
                        variant="outline",
                        margin_right="5px",
                        color=rx.color_mode_cond(light="white", dark="black"),
                        width="100px",
                        background_color=rx.color_mode_cond(light="black", dark="white"),
                        border_color="lightgreen",
                    ),
                    rx.button(
                        rx.link(
                            "login", href=reflex_local_auth.routes.LOGIN_ROUTE, underline="none",color=rx.color_mode_cond(light="black", dark="white"),),
                            size="3",
                            margin_right="40px",
                            color="black",
                            width="100px",
                            bg="skyblue",


                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align="center"
            ),
        ),
        background_color=rx.color_mode_cond(light="black", dark="white"),
        padding="1em",
        position="fixed",
        width="100%",
    )

class Spline(rx.Component):
    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]

spline = Spline.create
#link for the animation on Spline
scene = "https://prod.spline.design/WgCVJEkCUF1CFaaP/scene.splinecode"


def index() -> rx.Component:
    return rx.box(
        navbar(),

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
#------------HOME PAGE----------------

#navbar with just the logo, routing to the home page
def navbar_plain():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.color_mode_cond(
                        light=rx.image(
                            src="/momentumLogo.png",
                            alt="Reflex Logo light",
                            height="4em",
                            padding_left="30px",
                        ),
                        dark=rx.image(
                            src="/momentumLogoBlack.png",
                            alt="Reflex Logo dark",
                            height="4em",
                            padding_left="30px",
                        ),
                    ),
                    underline="none",
                    href="/"
                ),

            ),
            justify="between",
            align="center"
        ),
        background_color=rx.color_mode_cond(light="black", dark="white"),
        padding="1em",
        #position="fixed",
        width="100%",
    )

#defining the table - an structure to store the sign up information user
class usersignupmodel1(rx.Model, table=True):
     name: str
     username: str
     password: str


def signUp() -> rx.Component:

    return rx.box(
        navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.signUpCard()
    )



#-----------------------------------
#Check the the sign in from the auth cards -
#learn
#-----------------------------------



def signIn() -> rx.Component:
    return rx.box(
        navbar_plain(),
        rx.color_mode.button(position="bottom-left"),
        authCards.loginCard(),
        align="center",
        width="100%",



    )


app = rx.App()

#reflex local auth pages
#login page local authentication

app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)

#what does auth system mean

#my program pages
app.add_page(index)
app.add_page(signUp, route="/signUp")
app.add_page(signIn, route="/login")
