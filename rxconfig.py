import reflex as rx
from decouple import config

# Get your DATABASE_URL from environment variables
DATABASE_URL = config("DATABASE_URL")

config = rx.Config(
    app_name="pythonProject",
    db_url=DATABASE_URL,
    plugins=[rx.plugins.TailwindV3Plugin()]
)
