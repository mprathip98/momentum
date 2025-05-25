from sqlite3 import IntegrityError
import reflex as rx
from sqlalchemy.exc import IntegrityError
from pythonProject import databaseTables
from pythonProject import navBars
from pythonProject import pythonProject
import bcrypt
from pythonProject import globalVariable



class signUpState(rx.State):

    form_data :dict = {}
    did_submit: bool = False
    timeleft: int = 5
    error_message: str = ""
    #
    async def handle_submit(self, form_data: dict):
        valid: bool = True
        validPassword: bool = True

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
                    db_entry = databaseTables.usersignupmodel1(
                        **form_data
                    )
                    session.add(db_entry)
                    session.commit()
                self.did_submit = True
                yield rx.toast.success(
                        title="Signup Success!",
                        description="Redirecting to Login",
                        duration=4000,
                        position="top-right"
                )
                #redirecting to login
                yield rx.redirect("/login")
            elif validPassword == False:
                yield rx.toast.error(
                    title="Password Error",
                    description="password has to be at least 8 characters long",
                    duration=4000,
                    position="top-left"
                )
            else:
                yield rx.toast.error(
                    title="Signup Error",
                    description="fill in ALL of the inputs",
                    duration=4000,
                    position="top-left"
                )

        except IntegrityError as e:
            #excepts integrity errors and displays a message at the bottom right
            if "UNIQUE constraint" in str(e.orig):
                yield rx.toast.error(
                    title="Signup Error",
                    description="Username already taken. Please choose another.",
                    #status="error",
                    duration=4000,
                    position="top-left"
                )
            yield


class signInState(rx.State):
    in_session: bool = True
    user_info: dict = {}
    valid_username: str = ""
    valid_name: str = ""

#gello
    async def sign_in(self, form_data: dict):
        global valid_username
        global valid_name
        username = form_data.get("username", "")
        password = form_data.get("password", "")
        with rx.session() as session:
            #sends a query to filter the values in the table based on username and password
            #the "first" function fetches the first result
            user = session.query(databaseTables.usersignupmodel1).filter_by(username=username, password=password).first()

        if user:
            self.valid_username=user.username
            self.valid_name=user.name
            globalVariable.current_username = user.username
            self.in_session = True
            yield rx.toast.success(
                title="Login success", position="top-right"
            )
            yield rx.redirect("/dashboard")
        else:
            self.in_session = False
            yield rx.toast.error(
                "Invalid username or password", position="top-left"
            )
