import reflex as rx
from sqlalchemy.dialects import plugins

config = rx.Config(
    app_name="pythonProject",
    db_url="sqlite:///reflex.db"
)

plugins=[
    rx.plugins.TailwindV3Plugin()
]
