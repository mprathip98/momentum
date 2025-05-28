import reflex as rx

config = rx.Config(
    app_name="pythonProject",
    db_url="postgresql://neondb_owner:npg_1ByUSnGcax9q@ep-withered-tooth-aabnsi1r-pooler.westus3.azure.neon.tech/neondb?sslmode=require",
    plugins=[rx.plugins.TailwindV3Plugin()]
)
