import reflex as rx
from pythonProject import models

class monthState(rx.State):
    @rx.var
    def retrieve(self) -> dict:
        logs = {}
        with rx.session() as session:
            users = session.query(models.usersignupmodel1).all()
            for user in users:
                count = session.query(models.habitlog).filter_by(username=user.username).count()
                logs[user.username] = count
        return logs


class yearState(rx.State):
    pass

class lifetimeState(rx.State):
    pass

#