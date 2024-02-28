from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yaml

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

global returnObj
global pula

with open('pytania.yaml', 'r') as file:
    pula = yaml.safe_load(file)

returnObj: dict = {
    "question": "Pytanie",
    "answers": ["-----------"],
    "answers_uncovered": ["-----------"],
    "answers_points": [0],
    "answers_points_uncovered": [0],
    "exes": 0,
    "pula": 0,
    "points_blu": 0,
    "points_red": 0,
}

@api.get("/")
async def root():
    return returnObj

@api.get("/addpoints/{team}/{number}")
async def addpoints(team, number: int):
    if team == "blu":
        returnObj["points_blu"]+=number
        return returnObj["points_blu"]
    else:
        returnObj["points_red"] += number
        return returnObj["points_red"]

@api.get("/next_q")
async def next_question():
    top = pula[0]
    if len(pula) > 1:
        pula.pop(0)
    
    returnObj["question"] = top["pytanie"]
    returnObj["answers"] = []
    returnObj["answers_uncovered"] = []
    returnObj["answers_points_uncovered"] = []
    returnObj["answers_points"] = []
    returnObj["exes"]=0
    returnObj["pula"]=0
    for i in top["odpowiedzi"]:
        returnObj["answers"].append("-----------")
        returnObj["answers_points"].append(0)
        returnObj["answers_uncovered"].append(i[0])
        returnObj["answers_points_uncovered"].append(i[1])
    return top

@api.get("/uncover/{number}")
async def uncover(number: int):
    number -= 1
    returnObj["answers"][number] = returnObj["answers_uncovered"][number]
    returnObj["answers_points"][number] = returnObj["answers_points_uncovered"][number]
    returnObj["pula"] += returnObj["answers_points"][number]
    return returnObj

@api.get("/uncover_all/")
async def uncover_all():
    for i in range(len(returnObj["answers"])):
        returnObj["answers"][i] = returnObj["answers_uncovered"][i]
        returnObj["answers_points"][i] = returnObj["answers_points_uncovered"][i]
    return returnObj

@api.get("/exes/add")
async def add_exes():
    returnObj["exes"]+=1
    return returnObj["exes"]

@api.get("/exes/reset")
async def reset_exes():
    returnObj["exes"]=0
    return returnObj["exes"]