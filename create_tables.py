from reflex_local_auth import local_auth
from reflex.database import engine

def create_tables():
    local_auth.LocalUser.metadata.create_all(engine)
    local_auth.LocalAuthSession.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
    print("Tables created!")
