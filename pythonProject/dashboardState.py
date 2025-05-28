import reflex as rx



class dashboard(rx.State):
    habits=""
    async def dashSetter(self):
        global habits
        from pythonProject import globalVariable
        from pythonProject import models
        loggedInUsername = globalVariable.current_username
        with rx.session() as session:
            habits = session.query(models.Habit).filter_by(username=loggedInUsername).all()
            print(habits)
def dashboardSetter():
    print(dashboard.habits)