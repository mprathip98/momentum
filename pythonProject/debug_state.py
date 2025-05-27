# debug_state.py
import os
import reflex as rx

class DebugState(rx.State):
    def get_db_url(self):
        return os.getenv("DATABASE_URL") or "None"