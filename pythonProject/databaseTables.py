import reflex as rx
from pythonProject import authStates
from pythonProject import authCards
from pythonProject import navBars

#defining the table - an structure to store the sign up information user
class usersignupmodel1(rx.Model, table=True):
     name: str
     username: str
     password: str

#need to create a new table for the habits added
class Habit(rx.Model, table=True):
     habit_Name: str
     username: str
     description: str

class habitLog(rx.Model, table=True):
     username: str
     habit_Name: str
     date: str
     status: bool
