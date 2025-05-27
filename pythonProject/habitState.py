import reflex as rx
from pythonProject import authCards
from pythonProject import models
from pythonProject import globalVariable
from sqlalchemy.exc import IntegrityError
from pythonProject import navBars
from pythonProject.models import Habit


class State(rx.State):
    loggedInUsername: str = ""

class AddState(rx.State):
    form_data: dict = {}
    did_submit: str = False

    async def handle_submit(self, form_data: dict):
        validHabitName = True
        try:
            State.loggedInUsername = globalVariable.current_username
            print(State.loggedInUsername)
            form_data['username'] = State.loggedInUsername

            data={}
            with rx.session() as session:
                habits = session.query(Habit).filter_by(username=State.loggedInUsername, habit_Name=form_data["habit_Name"]).all()

            validHabitName = False if habits != [] else True

            if validHabitName:
                for k,v in form_data.items():
                    if v=="" or v==None:
                        yield rx.toast.warning(title="FILL ALL OF THE INPUTS", position="top-left")
                    else:
                        data[k]=v
                with rx.session() as session:
                    db_entry = models.Habit(
                        **data
                    )
                    #testing time
                    session.add(db_entry)
                    session.commit()
                    yield rx.toast.success(title="Habit Created!",
                                           description="You are a step closer to achieving you goal!",
                                           position="top-right")
                    yield rx.redirect("/track")
            elif not validHabitName:
                yield rx.toast.warning(title="Habit Already Exists", position="top-left")

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



class habitLog(rx.State):
    form_data: dict = {}

    async def handle_submit(self, form_data: dict):
        validLog = True
        try:
            for k, v in form_data.items():
                if k == "status":
                    if v == "crushed it":
                        form_data['status'] = True
                    else:
                        form_data['status'] = False
            form_data["username"] = globalVariable.current_username

            with rx.session() as session:
                logs = session.query(models.habitLog).filter_by(username=form_data["username"], date=form_data["date"], habit_Name=form_data["habit_Name"]).all()

            validLog = False if logs != [] else True

            if validLog:
                with rx.session() as session:
                    db_entry = models.habitLog(
                        **form_data
                    )
                    session.add(db_entry)
                    session.commit()
                yield rx.toast.success(title="Log Created!")
                yield rx.redirect("/dashboard")

            elif not validLog:
                yield rx.toast.warning("You already created a log for this date!")

#bro why is there an error
        except IntegrityError as e:
            #excepts integrity errors and displays a message at the bottom right
            if "UNIQUE constraint" in str(e.orig):
                yield rx.toast.warning(
                    title="",
                    description="You already created a log for this day",
                    #status="error",
                    duration=4000,
                    position="top-left"
                )

