from fastapi import APIRouter, HTTPException
from services.gemini_service import get_gemini_response
from services.qdrant_service import upsert_vector
import numpy as np
from schemas.task_generator_schemas import TaskRequest, TaskResponse 
router = APIRouter()



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

        lines = ai_response.strip().split("\n", 1)
        task_title = lines[0] if lines else "Generated Task"
        task_description = lines[1] if len(lines) > 1 else "No description provided."

        dummy_vector = np.random.rand(1536).tolist()
        payload = {
            "team_id": data.team_id,
            "context": data.context,
            "task_title": task_title,
            "task_description": task_description
        }
        upsert_vector(collection_name="task_collection", vector=dummy_vector, payload=payload)

        return TaskResponse(task_title=task_title, task_description=task_description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
