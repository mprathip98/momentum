import reflex as rx
import reflex_local_auth
from pythonProject import databaseTables
from pythonProject import authStates
from pythonProject import authCards
from pythonProject import navBars

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


def dashboardNavbar():
    #print(authStates.State.user)
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
                    rx.link(
                        "Track",
                        href="/",
                        underline="none",
                        size="6",
                        weight="medium",
                        color="skyblue",
                        margin_right="25px",
                    )
                    ,
                    rx.link(
                        "Add",
                        href="/",
                        weight="medium",
                        underline="none",
                        size="6",
                        color="skyblue"),
                ),
                rx.hstack(
                    rx.cond(

                        authStates.signInState.valid_username != "",
                        rx.text(
                            f"Welcome, {authStates.signInState.valid_name}!",
                            color="skyblue", size="6",
                            weight="bold",
                            margin_right="45px"),
                    ),
                    justify="end",
                ),


                justify="between",
                align="center"
            ),
        ),
        background_color=rx.color_mode_cond(light="black", dark="white"),
        padding="1em",
        width="100%",

    )