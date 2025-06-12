import reflex as rx
from pythonProject import authCards
from pythonProject import models
from pythonProject import globalVariable
from sqlalchemy.exc import IntegrityError
from pythonProject import navBars
from pythonProject.models import habit
from datetime import datetime


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
                habits = session.query(habit).filter_by(username=State.loggedInUsername, habit_Name=form_data["habit_Name"]).all()

            validHabitName = False if habits != [] else True

            if validHabitName:
                for k,v in form_data.items():
                    if v=="" or v==None:
                        yield rx.toast.warning(title="FILL ALL OF THE INPUTS", position="top-left")
                    else:
                        data[k]=v
                with rx.session() as session:
                    db_entry = models.habit(
                        **data
                    )
                    #testing time
                    session.add(db_entry)
                    session.commit()
                    yield rx.toast.success(title="Habit Created!",
                                           description="You are a step closer to achieving your goal!",
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
        valid_date = True
        try:
            for k, v in form_data.items():
                if k == "status":
                    if v == "crushed it":
                        form_data['status'] = True
                    else:
                        form_data['status'] = False
            form_data["username"] = globalVariable.current_username
            todayDate = datetime.today()
            userDate = int(form_data['date'][:4])+int(form_data['date'][5:7])+int(form_data['date'][8:])
            validDate = int(todayDate.strftime("%Y"))+int(todayDate.strftime("%m"))+int(todayDate.strftime("%d"))
            oldestDate = int(todayDate.strftime("%Y"))-100+int(todayDate.strftime("%m"))+int(todayDate.strftime("%d"))
            
            if userDate > validDate or userDate < oldestDate:
                valid_date = False

            with rx.session() as session:
                logs = session.query(models.habitlog).filter_by(username=form_data["username"], date=form_data["date"], habit_Name=form_data["habit_Name"]).all()

            validLog = False if logs != [] else True

            if validLog and valid_date:
                with rx.session() as session:
                    db_entry = models.habitlog(
                        **form_data
                    )
                    session.add(db_entry)
                    session.commit()
                yield rx.toast.success(title="Log Created!")
                yield rx.redirect("/dashboard")

            elif not validLog:
                yield rx.toast.warning("You already created a log for this date!", position="top-left")

            elif not valid_date:
                yield rx.toast.warning("Please enter a valid date!", position="top-left")

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
