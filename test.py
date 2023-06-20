import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

function_descriptions = [
    {
        "name": "calculate_deal_size",
        "description": "extract order details information, including which product clients want to buy, how many they want to buy, and return results in an array",
        "parameters": {
            "type": "object",
            "properties": {
                "orders": {
                    "type": "array",
                    "description": "an array of products people want to buy & the amount they want to buy",
                    "items": {
                        "product": {
                            "type": "string",
                            "description": "the product name that user wants to buy"
                        },
                        "amount": {
                            "type": "string",
                            "description": "the amount that user wants to buy for the speciifc product"
                        }
                    }
                }
            },
            "required": ["product", "amount"]
        }
    }
]


# function_descriptions = [
#     {
#         "name": "calculate_deal_size",
#         "description": "extract order details information, including which product clients want to buy, how many they want to buy, and calculate the deal size",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "dealSize":{
#                     "type": "string",
#                     "description": "the deal size calculated based on which products people want to buy, how many they want to buy, as well as the product catalogue unit price"
#                 }
#             },
#             "required": ["dealSize"]
#         }
#     }
# ]


content = """
Hi,
we are a team of 10 people, i want 2 t shirt & 1 pant for each member, and i will get 5 pairs of shoes;

can you let me know the price and how soon can it be delivered?

thanks
"""

product_catalogue = """
[{"product": "t-shirt", "price": "$23"}, {"product": "pants", "price": "$15"}, {"product": "shoes", "price": "$39"}]
"""

query =  f"This is the product catalogue: {product_catalogue} Please calculate the deal size:{content}"

messages = [{"role": "user", "content": query}]

response = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=messages,
    functions = function_descriptions,
    function_call="auto"
)

print(response)