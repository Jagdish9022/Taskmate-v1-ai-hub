from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.gemini_service import get_gemini_response

router = APIRouter()

class TaskRequest(BaseModel):
    team_id: str
    context: str  # e.g., project goal, sprint theme, or task focus

class TaskResponse(BaseModel):
    task_title: str
    task_description: str

@router.post("/", response_model=TaskResponse)
async def generate_task(data: TaskRequest):
    try:
        prompt = (
            f"Generate a single task for the following context:\n\n"
            f"{data.context.strip()}\n\n"
            f"Respond with a concise task title and a short description suitable for a team with ID {data.team_id}. "
            f"Keep it clear and actionable."
        )
        ai_response = get_gemini_response(prompt)

        # You can enhance this with parsing logic if needed
        lines = ai_response.strip().split("\n", 1)
        task_title = lines[0] if lines else "Generated Task"
        task_description = lines[1] if len(lines) > 1 else "No description provided."

        return TaskResponse(task_title=task_title, task_description=task_description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
