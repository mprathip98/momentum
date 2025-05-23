import reflex as rx
from pygments.styles.dracula import background
from reflex.components.radix.primitives.form import FormSubmit

from rxconfig import config


class State(rx.State):
    pass


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
                            "login", href="/login", underline="none",color=rx.color_mode_cond(light="black", dark="white"),),
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

        rx.color_mode.button(position="bottom-right"),
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
                    "GET READY TO",
                    size="9",
                    position="center",
                    color="skyblue",
                    margin_top="12%",
                ),
                rx.heading(
                    "CHANGE YOUR",
                    size="9",
                    position="center",
                    color="skyblue",
                ),
                rx.heading(
                    "HABITS TODAY",
                    size="9",
                    background_image="linear-gradient(to right, #FFFFFF, #6960ff)",  # Gradient from red to green
                    background_clip="text",
                    font_weight="bold",
                    color="transparent",
                ),
                rx.button(
                    rx.link("Get Started", href="/signUp", color="black", underline="none"),
                            size="4",
                            color="black",
                            width="250px",
                            margin_top="30px",
                            height="60px",
                            bg="skyblue",
                            margin_left="75px",
                            border_radius="15px",
                            style= {
                                "font-weight": "bold",
                                "font-optical-sizing": "auto",
                                "font-style": "normal",
                                "font_size":  "2em",
                            }
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
class userSignUpModel(rx.Model, table=True):
    name: str
    username: str
    password: str

#handling the signUp info
class signUpState(rx.State):
    form_data :dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        print(form_data)
        with rx.session() as session:
            db_entry = userSignUpModel(
                **form_data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield




def signUp() -> rx.Component:

    return rx.box(
        navbar_plain(),
        rx.card(
            rx.center(
                rx.form(
                    rx.vstack(
                        rx.color_mode_cond(
                            dark=rx.image(
                                src="/momentumLogo.png",
                                alt="Reflex Logo light",
                                height="4em",
                                margin_top="5%"),

                            light=rx.image(
                                src="/momentumLogoBlack.png",
                                alt="Reflex Logo dark",
                                height="4em",
                                margin_top="5%"),
                        ),

                        rx.heading("Create an account", size="5", margin_bottom="20px"),

                        rx.vstack(
                            rx.text(
                                "name *",
                                size="4",
                                text_align="left",
                                weight="medium",
                                width="100%"
                            ),
                            rx.input(
                                name="name",
                                required=True,
                                placeholder="John Doe",
                                type="text",
                                width="300px",
                                size="3",
                                margin="-2%"
                            ),
                            margin="2%",
                        ),
                        rx.vstack(
                            rx.text(
                                "username *",
                                size="4",
                                text_align="left",
                                weight="medium",
                                width="100%"
                            ),
                            rx.input(
                                type="text",
                                name="username",
                                required=True,
                                placeholder="bigManJohn",
                                width="300px",
                                size="3",
                                margin="-2%"
                            ),
                            margin="2%",
                        ),

                        rx.vstack(
                            rx.text(
                                "password *",
                                size="4",
                                required=True,
                                name="password",
                                text_align="left",
                                weight="medium",
                                width="100%"
                            ),
                            rx.input(
                                width="300px",
                                size="3",
                                margin="-2%",
                                type="password",
                            ),
                            margin="2%",
                            margin_bottom="10%",
                        ),
                        rx.button(
                            "Create",
                            width="30%",
                            size="3",
                            margin_left="-3%",
                            align="center",
                            font_weight="bold",
                            font_size="1em",
                            type="submit",
                        ),
                        rx.link(
                            "I already have an account tho...",
                            margin="3%",
                            margin_bottom="5%",
                            href="/login",
                            width="100%",
                            text_align="center",
                        ),

                        align="center",
                        border_color="white",
                    ),

                    align="center",
                    #on_submit=signUpState.handle_submit(),
                    #reset_on_submit=True,

                ),
            ),
            width="35%",
            align="center",
            margin="2%",
            margin_left="32%"

        ),
        align="center",
        width="100%",
    )


def signIn() -> rx.Component:
    return rx.box(
        navbar_plain(),
        rx.card(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/momentumLogo.png",
                        alt="Reflex Logo light",
                        height="4em",
                        margin_top="5%"
                    ),
                    rx.heading("Sign Back In", size="5", margin_bottom="20px", font="Oswald Bold"),

                    rx.vstack(
                        rx.text("username", size="4"),
                        rx.input(
                            placeholder="bigManJohn",
                            width="300px",
                            size="3",
                            margin_top="-2%",
                            margin_bottom="5%",
                        ),
                    ),
                    rx.vstack(
                        rx.text("password", size="4"),
                        rx.input(
                            type="password",
                            width="300px",
                            margin_top="-2%",
                            margin_bottom="10%",
                            size="3"
                        ),
                    ),

                    rx.button(
                        "Login",
                        width="65%",
                        size="3",
                        align="center",
                        font_weight="bold",
                        font_size="1em",
                        type="submit",

                    ),
                    rx.link(
                        "I do not have an account tho...",
                        href="/signUp",
                        width="100%",
                        text_align="center",
                        margin_top="3%",
                        margin_bottom="5%",
                    ),

                    align="center",
                    border_color="white",
                ),

            ),
            width="35%",
            justify="center",
            margin_top="5%",
            margin_left="32%",

        ),
        align="center",
        width="100%",


)


app = rx.App()
app.add_page(index)
app.add_page(signUp, route="/signUp")
app.add_page(signIn, route="/login")

