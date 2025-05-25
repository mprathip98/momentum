import reflex as rx
from pythonProject import authCards
from pythonProject import databaseTables
from pythonProject import globalVariable
from sqlalchemy.exc import IntegrityError
from pythonProject import navBars

class State(rx.State):
    loggedInUsername: str = ""

class AddState(rx.State):
    form_data: dict = {}
    did_submit: str = False


    async def handle_submit(self, form_data: dict):
        try:
            State.loggedInUsername = globalVariable.current_username
            form_data['username'] = State.loggedInUsername
            data={}
            for k,v in form_data.items():
                if v=="" or v==None:
                    yield rx.toast.warning(title="FILL ALL OF THE INPUTS", position="top-left")
                else:
                    data[k]=v


            with rx.session() as session:
                db_entry = databaseTables.Habit(
                    **data

                )
                session.add(db_entry)
                session.commit()
                yield rx.toast.success(title="Habit Created!",
                                       description="You are a step closer to achieving you goal!",
                                       position="top-right")
                yield rx.redirect("/track")
        except IntegrityError as e:
            #excepts integrity errors and displays a message at the bottom right
            if "UNIQUE constraint" in str(e.orig):
                yield rx.toast.warning(
                    title="",
                    description="Habit Already Exists!",
                    #status="error",
                    duration=4000,
                    position="top-left"
                )
