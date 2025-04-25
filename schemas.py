from pydantic import BaseModel
from typing import Literal

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    role: Literal["user", "assistant"]
    content: str
