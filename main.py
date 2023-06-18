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


# email = """
# Cyriac Kodath <cyriac.kodath@gmail.com>
# Sat, 17 Jun, 09:38 (1 day ago)
# to Jason.zhou.design

# Hello Jason, 

# I got your email from your youtube channel (really great videos by the way!) and wanted to write to you about using Chat GPT in Algorithmic Trading. 

# A little intro about me, I have just finished a PhD in Economics from the UK a few months back and have experience with Quantitative models. I also have a basic knowledge of Python coding so have been able to follow your videos. Recently I released a course on Udemy about electronic market making and also set up a trading livestream as a proof of concept on my website (I will put the links below for you to take a look at). I was interested to scale this up and possibly improve it with AI models, though I am not quite sure how to go about this. Would love to have a chat about this, if you are interested?

# Best wishes,

# Cyriac Kodath

# Udemy Course: https://www.udemy.com/course/electronic-market-making-with-angel-one-smart-api/?referralCode=1B5D076540D2986BEFEF
# LinkedIn: https://www.linkedin.com/in/cyriackodath/
# YouTube Channel: https://www.youtube.com/@AlgoTraderOnline/streams
# Website: https://www.algotrader.online/
# """

# query = f"Please extract key information from this email: {email} "

# messages = [{"role": "user", "content": query}]

# response = openai.ChatCompletion.create(
#     model="gpt-4-0613",
#     messages=messages,
#     functions = function_descriptions,
#     function_call="auto"
# )

# print(response)


class Email(BaseModel):
    from_email: str
    content: str


emails = {
    0: Email(from_email="cyriac.kodath@gmail.com",
             content = """
                Hello Jason, 

                I got your email from your youtube channel (really great videos by the way!) and wanted to write to you about using Chat GPT in Algorithmic Trading. 

                A little intro about me, I have just finished a PhD in Economics from the UK a few months back and have experience with Quantitative models. I also have a basic knowledge of Python coding so have been able to follow your videos. Recently I released a course on Udemy about electronic market making and also set up a trading livestream as a proof of concept on my website (I will put the links below for you to take a look at). I was interested to scale this up and possibly improve it with AI models, though I am not quite sure how to go about this. Would love to have a chat about this, if you are interested?

                Best wishes,

                Cyriac Kodath

                Udemy Course: https://www.udemy.com/course/electronic-market-making-with-angel-one-smart-api/?referralCode=1B5D076540D2986BEFEF
                LinkedIn: https://www.linkedin.com/in/cyriackodath/
                YouTube Channel: https://www.youtube.com/@AlgoTraderOnline/streams
                Website: https://www.algotrader.online/
             """
             )
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def analyse_email(email: Email):
    # query = f"Please extract key information from this email: {email} "

    # messages = [{"role": "user", "content": query}]

    # response = openai.ChatCompletion.create(
    #     model="gpt-4-0613",
    #     messages=messages,
    #     functions = function_descriptions,
    #     function_call="auto"
    # )

    return {"email": email}