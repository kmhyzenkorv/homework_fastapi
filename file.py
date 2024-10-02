from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberOfBrigade(BaseModel):
    id: int
    name: str

class TeamWorkExperience(BaseModel):
    id: int
    name: str
    experience: float

class UserInfo(BaseModel):
    id: int
    login: str

NUMBER_OF_BRIGADE_DB = [

    NumberOfBrigade(id= 1, name="Бригада Чижики"),
    NumberOfBrigade(id= 2, name="Строй Гастрики"),
    NumberOfBrigade(id= 3, name="Демодворики"),
]

TEAM_WORK_EXPERIENCE_DB = [

    TeamWorkExperience(id= 1, name= "Бригада Чижики", experience= 5.5),
    TeamWorkExperience(id= 2, name="Строй Гастрики", experience= 3.0),
    TeamWorkExperience(id= 3, name="Демодворики", experience= 1.243),
]

USER_INFO_DB = [

    UserInfo(id= 1, login="Сергей"),
    UserInfo(id= 2, login="Анатолий"),
    UserInfo(id= 3, login="Александр"),
]

@app.get("/")
async def root():
    return {"message": "Домашняя работа"}


@app.get("/brigade/{brigade_id}")
def number_of_the_brigades(brigade_id: int):
    for brigade in NUMBER_OF_BRIGADE_DB:
        if brigade.id == brigade_id:
            return brigade
        
@app.get("/brigade/")
def brigades():
    return TEAM_WORK_EXPERIENCE_DB

@app.get("/UserInfo/")
def users():
    return USER_INFO_DB

@app.get("/UserInfo/{users_id}")
def users(users_id: int):
    for users in USER_INFO_DB:
        if users.id == users_id:
            return users
        
@app.get("/experience/{experience_id}")
def experience_of_the_brigades(experience_id: int):
    for experience in TEAM_WORK_EXPERIENCE_DB:
        if experience.id == experience_id:
            return experience

@app.get("/experience/")
def users():
    return TEAM_WORK_EXPERIENCE_DB