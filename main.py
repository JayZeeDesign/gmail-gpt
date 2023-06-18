import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

function_descriptions = [
    {
        "name": "extract_info_from_email",
        "description": "categorise & extract key info from an email, such as use case, company name, contact details, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "companyName": {
                    "type": "string",
                    "description": "the name of the company that sent the email"
                },
                "useCase": {
                    "type": "string",
                    "description": "The purpose & use case of this company's enquiry"
                },
                "contactDetails": {
                    "type": "string",
                    "description": "The contact details of the person who sent the email"
                },
                "priority": {
                    "type": "string",
                    "description": "Try to give a priority score to this email based on how likely this email will leads to a good business opportunity for AI consulting, from 0 to 10; 10 most important"
                },
                "category": {
                    "type": "string",
                    "description": "Try to categorise this email into categories like those: 1. customer support; 2. consulting; 3. job; 4. partnership; etc."
                },
                "nextStep":{
                    "type": "string",
                    "description": "What is the suggested next step to move this forward?"
                }
            },
        }
    }
]


class Email(BaseModel):
    from_email: str
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def analyse_email(email: Email):
    content = email.content
    query = f"Please extract key information from this email: {content} "

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions = function_descriptions,
        function_call="auto"
    )

    return {"email": email}