import reflex as rx
from starlette.websockets import WebSocket
from pythonProject import models
from pythonProject import globalVariable
from pythonProject.models import usersignupmodel1
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
load_dotenv()

import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

def send_signup_email(to_email):
    try:
        message = Mail(
            from_email='momentumhabitdaily@gmail.com',
            to_emails=to_email,
            subject="Welcome to Momentum!",
            html_content="""
                         <h1><strong>Thanks for signing up!</strong></h1> 
                         <p>Get ready to start your journey with Momentum!</p> 
                         <image src='/momentumLogoBlack.png'>
                         """
        )
        #alr i know what to do
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(f"Error sending email: {e}")



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
                name1 = form_data["name"]
                username1 = form_data["username"]
                password1 = form_data["password"]
                email1 = form_data["email"]
                with rx.session() as session:
                    #try to check before creating a signup page
                    db_entry = usersignupmodel1(
                        name=name1,
                        username=username1,
                        email=email1,
                        password=password1,
                    )

                    session.add(db_entry)
                    session.commit()
                    session.close()

                    self.did_submit = True
                yield rx.toast.success(
                        title="Signup Success!",
                        description="Redirecting to Login",
                        duration=4000,
                        position="top-right"
                )
                #redirecting to login
                yield rx.redirect("/loginRedirection")
                send_signup_email(form_data["email"])
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

        except Exception as e:
            #excepts integrity errors and displays a message at the bottom right

            print(e)
            yield rx.toast.error(
                title="Signup Error",
                description="Username already taken. Please choose another.",
                #status="error",
                # duration=4000,
                position="top-left"
                )
            yield
            if e == WebSocket:
                yield rx.toast.error("Check you internet connection and try again in a little while",position="top-left")

class signInState(rx.State):
    in_session: bool = True
    user_info: dict = {}
    valid_username: str = ""
    valid_name: str = ""


    async def sign_in(self, form_data: dict):
        global valid_username
        global valid_name
        try:
            username = form_data.get("username", "")
            password = form_data.get("password", "")
            with rx.session() as session:
                # sends a query to filter the values in the table based on username and password
                # the "first" function fetches the first result
                user = session.query(models.usersignupmodel1).filter_by(username=username, password=password).first()

            if user:
                self.valid_username = user.username
                self.valid_name = user.name
                globalVariable.current_username = user.username
                self.in_session = True
                yield rx.toast.success(
                    title="Login success", position="top-right"
                )
                yield rx.redirect("/dashboard")
                # print(globalVariable.TrackState.habits if globalVariable.current_username != "" else []),
            else:
                self.in_session = False
                yield rx.toast.error(
                    "Invalid username or password", position="top-left"
                )
        except Exception as e:
            print(e)
            yield rx.toast.error("Check you internet connection and try again in a little while", position="top-left")

