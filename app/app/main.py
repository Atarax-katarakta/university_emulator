import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/education_approve/")
async def education(minimal_ege: int, student_ege: int):
    return {'answer': minimal_ege <= student_ege}


@app.post("/payment/")
async def payment_complete():
    return {'answer': 'Вы поступили'}
