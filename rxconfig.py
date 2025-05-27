import reflex as rx
from sqlalchemy.dialects import plugins
from decouple import config

DATABASE_URL = config("DATABASE_URL")

config = rx.Config(
    app_name="pythonProject",
    db_url="sqlite:///reflex.db",
    plugins=[rx.plugins.TailwindV3Plugin()]
)
