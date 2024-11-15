""" Implement RAG with Cohere """
import json
from typing import List
from fastapi import FastAPI, HTTPException, Body, Request

import cohere
import numpy as np


# documents = [
#     {
#         "data": {
#             "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
#         }
#     },
#     {
#         "data": {
#             "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
#         }
#     },
#     {
#         "data": {
#             "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
#         }
#     }
# ]


co = cohere.ClientV2(
    api_key="UWrufrRl3IP6IR3T8iV4JzB5EZof8rpwEVm0Nz5G",
)

# Add the user query
# query = "Are there health benefits?"
# query = "Is it possible to work remotely?"

# Generate the response
# response = co.chat(model="command-r-plus-08-2024",
#                    messages=[{'role': 'user', 'content': query}], documents=documents)


# chat = co.chat(
#     message="hello world!",
#     model="command"
# )

# print(chat)
# print(response.message.content[0].text)

# if response.message.citations:
#     print("\nCITATIONS:")
#     for citation in response.message.citations:
#         print(citation, "\n")


app = FastAPI()


@app.post("/basic-rag/")
async def handlerag(request: Request):
    reqBody = await request.json()
    reqDocuments = reqBody['documents']
    reqQuery = reqBody['query']

    response = co.chat(model="command-r-plus-08-2024",
                       messages=[{'role': 'user', 'content': reqQuery}], documents=reqDocuments)

    return response.message.content


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
