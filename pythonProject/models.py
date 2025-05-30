import reflex as rx
from sqlmodel import Field
import sqlalchemy
from dotenv import load_dotenv
load_dotenv()

#defining the table - an structure to store the sign up information user
class usersignupmodel1(rx.Model, table=True):
     name: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     username: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
          unique=True,
     )
     password: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )



#need to create a new table for the habits added
class habit(rx.Model, table=True):
     habit_Name: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     username: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     description: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )

class habitlog(rx.Model, table=True):
     username: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     habit_Name: str = Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     date: str =  Field(
          sa_type=sqlalchemy.String,
          nullable=False,
     )
     status: bool = Field(
          sa_type=sqlalchemy.Boolean,
          nullable=False,
     )