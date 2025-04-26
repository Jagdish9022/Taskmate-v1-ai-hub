from pydantic import BaseModel

class EODRequest(BaseModel):
    user_id: str
    activities: str

class EODResponse(BaseModel):
    content: str