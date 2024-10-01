from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number_of_brigade(BaseModel):
    id: int
    name: str

class Team_work_experience(BaseModel):
    id: int
    name: str
    experience: float

class User_info(BaseModel):
    id: int
    login: str

Number_of_brigade_db = [

    Number_of_brigade(id= 1, name="Бригада Чижики"),
    Number_of_brigade(id= 2, name="Строй Гастрики"),
    Number_of_brigade(id= 3, name="Демодворики"),
]

Team_work_experience_db = [

    Team_work_experience(id= 1, name= "Бригада Чижики", experience= 5.5),
    Team_work_experience(id= 2, name="Строй Гастрики", experience= 3.0),
    Team_work_experience(id= 3, name="Демодворики", experience= 1.243),
]

User_info_db = [

    User_info(id= 1, login="Сергей"),
    User_info(id= 2, login="Анатолий"),
    User_info(id= 3, login="Александр"),
]

@app.get("/")
async def root():
    return {"message": "Домашняя работа"}


@app.get("/brigade/{brigade_id}")
def NofB(brigade_id: int):
    for brigade in Number_of_brigade_db:
        if brigade.id == brigade_id:
            return brigade
        
@app.get("/brigade/")
def brigades():
    return Team_work_experience_db

@app.get("/user_info/")
def users():
    return User_info_db

@app.get("/user_info/{users_id}")
def users(users_id: int):
    for users in User_info_db:
        if users.id == users_id:
            return users
        
@app.get("/experience/{experience_id}")
def NofB(experience_id: int):
    for experience in Team_work_experience_db:
        if experience.id == experience_id:
            return experience

@app.get("/experience/")
def users():
    return Team_work_experience_db