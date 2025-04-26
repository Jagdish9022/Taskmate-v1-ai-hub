from pydantic import BaseModel
from typing import Literal

class TaskRequest(BaseModel):
    team_id: str
    context: str  
class TaskResponse(BaseModel):
    task_title: str
    task_description: str