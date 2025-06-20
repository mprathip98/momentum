import reflex as rx
from pythonProject import authStates


def signUpCard():
    return rx.box(
        rx.mobile_only(
            rx.center(
                rx.form(
                    rx.vstack(
                        rx.color_mode_cond(
                            dark=rx.image(
                                src="/momentumLogo.png",
                                alt="Reflex Logo light",
                                height="2em",
                                margin_top="1%"),

                            light=rx.image(
                                src="/momentumLogoBlack.png",
                                alt="Reflex Logo dark",
                                height="2em",
                                margin_top="1%"),
                        ),

                        rx.heading("Create an account", size="2"),
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "name",
                                    size="4",
                                    text_align="left",
                                    weight="medium",
                                    width="100%",
                                    margin_left="-25%"
                                ),
                                rx.input(
                                    name="name",
                                    required=True,
                                    placeholder="John Doe",
                                    type="text",
                                    width="150%",
                                    size="3",
                                    margin_top="-2%",
                                    margin_left="-25%"

                                ),
                                margin="1%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "email",
                                    size="4",
                                    text_align="left",
                                    weight="medium",
                                    width="100%",
                                    margin_left="-25%"
                                ),
                                rx.input(
                                    type="email",
                                    name="email",
                                    required=True,
                                    placeholder="bigManJohn@gmail.com",
                                    width="150%",
                                    size="3",
                                    margin_top="-2%",
                                    margin_left="-25%"

                                ),
                                margin="1%",
                            ),
                        ),
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "username",
                                    size="4",
                                    text_align="left",
                                    weight="medium",
                                    width="100%",
                                    margin_left="-25%"
                                ),
                                rx.input(
                                    type="text",
                                    name="username",
                                    required=True,
                                    placeholder="bigManJohn",
                                    width="150%",
                                    size="3",
                                    margin_top="-2%",
                                    margin_left="-25%"
                                ),
                                margin="1%",
                            ),

                            rx.vstack(
                                rx.text(
                                    "password",
                                    size="4",
                                    required=True,
                                    name="password",
                                    text_align="left",
                                    weight="medium",
                                    width="100%",
                                    margin_left = "-25%"
                                ),
                                rx.input(
                                    width="150%",
                                    size="3",
                                    margin_top="-2%",
                                    name="password",
                                    type="password",
                                    margin_left="-25%"
                                ),
                                margin="1%",
                                margin_bottom="5%",
                            ),
                        ),

                        rx.button(
                            "Create",
                            width="40%",
                            size="3",
                            margin_top="3%",
                            align="center",
                            font_weight="bold",
                            font_size="1em",
                            type="submit",
                            # on_click=errorCheck,
                        ),
                        rx.link(
                            "I already have an account tho...",
                            margin_bottom="5%",
                            href="/login",
                            width="100%",
                            text_align="center",
                        ),

                        align="center",
                        border_color="white",
                    ),

                    align="center",
                    on_submit=authStates.signUpState.handle_submit,

                    reset_on_submit=True,
                ),
            ),
            width="80%",
            align="center",
            margin="2%",
            margin_top="10%",
            margin_left="10%",
            border_color="white",
            background_color=rx.color_mode_cond(light="white", dark="#121213"),
            class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        ),
        rx.desktop_only(
            rx.center(
                rx.form(
                    rx.vstack(
                        rx.color_mode_cond(
                            dark=rx.image(
                                src="/momentumLogo.png",
                                alt="Reflex Logo light",
                                height="4em",
                                margin_top="1%"),

                            light=rx.image(
                                src="/momentumLogoBlack.png",
                                alt="Reflex Logo dark",
                                height="4em",
                                margin_top="1%"),
                        ),

                        rx.heading("Create an account", size="5"),
                        rx.hstack(
                            rx.vstack(
                                rx.vstack(
                                    rx.text(
                                        "name",
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
                                        margin_top="-2%"
                                    ),
                                    margin="1%",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "email",
                                        size="4",
                                        text_align="left",
                                        weight="medium",
                                        width="100%"
                                    ),
                                    rx.input(
                                        type="email",
                                        name="email",
                                        required=True,
                                        placeholder="bigManJohn@gmail.com",
                                        width="300px",
                                        size="3",
                                        margin_top="-2%"
                                    ),
                                    margin="1%",
                                ),
                            ),
                            rx.vstack(
                                rx.vstack(
                                    rx.text(
                                        "username",
                                        size="4",
                                        text_align="right",
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
                                        margin_top="-2%"
                                    ),
                                    margin="1%",
                                ),

                                rx.vstack(
                                    rx.text(
                                        "password",
                                        size="4",
                                        required=True,
                                        name="password",
                                        text_align="right",
                                        weight="medium",
                                        width="100%"
                                    ),
                                    rx.input(
                                        width="300px",
                                        size="3",
                                        margin_top="-2%",
                                        name="password",
                                        type="password",
                                    ),
                                    margin="1%",
                                    margin_bottom="5%",
                                ),
                            ),
                        ),

                        rx.button(
                            "Create",
                            width="40%",
                            size="3",
                            margin_top="3%",
                            align="center",
                            font_weight="bold",
                            font_size="1em",
                            type="submit",
                            # on_click=errorCheck,
                        ),
                        rx.link(
                            "I already have an account tho...",
                            margin_bottom="5%",
                            href="/login",
                            width="100%",
                            text_align="center",
                        ),

                        align="center",
                        border_color="white",
                    ),

                    align="center",
                    on_submit=authStates.signUpState.handle_submit,

                    reset_on_submit=True,
                ),

            ),

            width="55%",
            align="center",
            margin="2%",
            margin_top="4%",
            margin_left="22%",
            border_color="white",
            background_color=rx.color_mode_cond(light="white", dark="#121213"),
            z_index="10",
            class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",
        ),
        z_index="10",

    ),


def loginCard():
    return rx.fragment(
        rx.desktop_only(
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
                        rx.heading("Sign Back In", size="5", margin_bottom="20px", font="Oswald Bold"),

                        rx.vstack(
                            rx.text("username", size="4"),
                            rx.input(
                                placeholder="bigManJohn",
                                name="username",
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
                                name="password",
                                width="300px",
                                margin_top="-2%",
                                margin_bottom="10%",
                                size="3"
                            ),
                        ),

                        rx.button(
                            "Login",
                            width="50%",
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
                    on_submit=authStates.signInState.sign_in,

                    reset_on_submit=True,
                ),
            ),
            width="35%",
            justify="center",
            margin_top="3%",
            margin_left="32%",
            background_color=rx.color_mode_cond(light="white", dark="#121213"),
            class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",

        ),
        rx.mobile_only(
            rx.center(

                rx.form(
                    rx.vstack(
                        rx.color_mode_cond(
                            dark=rx.image(
                                src="/momentumLogo.png",
                                alt="Reflex Logo light",
                                height="2em",
                                margin_top="5%"),

                            light=rx.image(
                                src="/momentumLogoBlack.png",
                                alt="Reflex Logo dark",
                                height="2em",
                                margin_top="5%"),
                        ),
                        rx.heading("Sign Back In", size="5", margin_bottom="20px", font="Oswald Bold"),

                        rx.vstack(
                            rx.text("username", size="3", margin_left="-25%"),
                            rx.input(
                                placeholder="bigManJohn",
                                name="username",
                                width="150%",
                                margin_top="-2%",
                                margin_bottom="10%",
                                margin_left="-25%",
                                size="3"
                            ),
                        ),
                        rx.vstack(
                            rx.text("password", size="4", margin_left="-25%"),
                            rx.input(
                                type="password",
                                name="password",
                                width="150%",
                                margin_top="-2%",
                                margin_bottom="10%",
                                margin_left="-25%",
                                size="3"
                            ),
                        ),

                        rx.button(
                            "Login",
                            width="50%",
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
                    on_submit=authStates.signInState.sign_in,

                    reset_on_submit=True,
                ),
            ),
            width="80%",
            justify="center",
            margin_top="15%",
            margin_left="10%",
            background_color=rx.color_mode_cond(light="white", dark="#121213"),
            class_name="flex flex-col items-center justify-center space-y-4 p-8 rounded-xl border-1 border-cyan-800 shadow-[0_0_15px_theme(colors.cyan.400)]",

        ),

    ),