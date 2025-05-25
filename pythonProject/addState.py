import reflex as rx
from pythonProject import cards
from pythonProject import databaseTables
from pythonProject import globalVariable
from pythonProject import navBars

class AddState(rx.State):
    form_data: dict = {}
    did_submit: str = False



    async def handle_submit(self, form_data: dict):
        from pythonProject.authStates import signInState
        from pythonProject import authStates
        username = globalVariable.current_username
        form_data['username'] = username

        with rx.session() as session:
            db_entry = databaseTables.Habit(
                **form_data

            )
            session.add(db_entry)
            session.commit()
            yield rx.toast.success("k")
