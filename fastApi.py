from cgitb import html
from html.entities import html5
from fastapi import FastAPI
#uvicorn fastApi:app --reload --port 2022

app = FastAPI()


#типо делаем url этодикоратор  путь /
@app.get("/",tags=["главная"]) #и типо делим на категории в fast api docs
def hello():
    """comment in func hello """
    return {
        f"lol":"ee\n"

    }

#типо параметр в юрл
@app.get("/1/{pk}")
def getKey(pk:int):
    """it is parametry k function"""
    return {f"key:{pk}"}

#типо параметр в юрл http://127.0.0.1:2022/2/1?q=lol
@app.get("/2/{pk}")
def getItem(pk:int,q:str=None): #типо какой параметр принимаем
    """it is parametry k function"""
    return {f"key:{pk} , str:{q}"}

@app.get("/users/{id}/iteams/{iteam}")
def getItem(id:int,iteam:str=None):
    return {f"users:{id} , iteam:{iteam}"}