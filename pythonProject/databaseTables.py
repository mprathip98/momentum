import reflex as rx
from pythonProject import databaseTables
from pythonProject import authStates
from pythonProject import authCards
from pythonProject import navBars

#defining the table - an structure to store the sign up information user
class usersignupmodel1(rx.Model, table=True):
     name: str
     username: str
     password: str