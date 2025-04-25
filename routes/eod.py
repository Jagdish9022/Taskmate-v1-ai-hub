from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.gemini_service import get_gemini_response

router = APIRouter()

class EODRequest(BaseModel):
    user_id: str
    activities: str

class EODResponse(BaseModel):
    content: str

@router.post("/", response_model=EODResponse)
async def generate_eod(data: EODRequest):
    try:
        prompt = (
            f"Generate a concise End Of Day (EOD) report based on these activities:\n\n"
            f"{data.activities.strip()}\n\n"
            "Include only the most important points in a short and clear format. Limit the report to a few sentences, focusing on key tasks and outcomes."
        )
        content = get_gemini_response(prompt)
        return EODResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
