from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chatbot import ChatBot

app = FastAPI()
chatbot = ChatBot()

class Message(BaseModel):
    content: str

@app.post("/chat")
async def chat(message: Message):
    try:
        response = chatbot.get_response(message.content)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))