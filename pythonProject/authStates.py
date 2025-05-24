from sqlite3 import IntegrityError
import reflex as rx
from pygments.styles.dracula import background
from reflex.components.radix.primitives.form import FormSubmit
from rich.jupyter import display
from sqlalchemy.exc import IntegrityError
import asyncio
import reflex_local_auth
from rxconfig import config
from pythonProject import pythonProject

class State(rx.State):
    user: dict = {}

class signUpState(rx.State):

    form_data :dict = {}
    did_submit: bool = False
    timeleft: int = 5
    error_message: str = ""
    #
    async def handle_submit(self, form_data: dict):
        valid: bool = True
        validPassword: bool = True
        #print(form_data)
        try:
            self.form_data = form_data
            data = {}
            for k, v in form_data.items():

                if v == "" or v is None or v == None:
                    valid = False
                else:
                    if k == "password" and len(v)<8:
                        validPassword = False
                    else:
                        data[k] = v

           #print(data)
            if valid and validPassword:
                with rx.session() as session:
                    #try to check before creating a sign up pag
                    db_entry = pythonProject.usersignupmodel1(
                        **form_data
                    )
                    session.add(db_entry)
                    session.commit()
                self.did_submit = True
                yield rx.toast.success(
                        title="Signup Success!",
                        description="Redirecting to Login",
                        duration=4000
                )
                #redirecting to login
                yield rx.redirect("/login")
            elif validPassword == False:
                yield rx.toast.error(
                    title="Password Error",
                    description="password has to be at least 8 characters long",
                    duration=4000
                )
            else:
                yield rx.toast.error(
                    title="Signup Error",
                    description="fill in ALL of the inputs",
                    duration=4000
                )

        except IntegrityError as e:
            #excepts integrity errors and displays a message at the bottom right
            if "UNIQUE constraint" in str(e.orig):
                yield rx.toast.error(
                    title="Signup Error",
                    description="Username already taken. Please choose another.",
                    #status="error",
                    duration=4000
                )
            yield


class signInState(rx.State):
    in_session: bool = True
#gello
    async def sign_in(self, form_data: dict):
        username = form_data.get("username", "")
        password = form_data.get("password", "")
        with rx.session() as session:
            #sends a query to filter the values in the table based on username and password
            #the "first" function fetches the first result
            State.user = session.query(pythonProject.usersignupmodel1).filter_by(username=username, password=password).first()
            print(State.user)
        #checks if there is something in user
        if State.user:
            self.in_session = True
            yield rx.toast.success(
                title="Login success",
            )
            yield rx.redirect("/")
        else:
            self.in_session = False
            yield rx.toast.error(
                "Invalid username or password"
            )