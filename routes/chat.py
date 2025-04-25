from fastapi import APIRouter, HTTPException
from schemas import ChatRequest, ChatResponse
from services.gemini_service import get_gemini_response
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.gemini_service import get_gemini_response

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(data: ChatRequest):
    try:
        reply = get_gemini_response(data.message)
        return ChatResponse(role="assistant", content=reply)
    except Exception as e:
        print("❌ Gemini ERROR:", str(e))  # <--- log the error
        raise HTTPException(status_code=500, detail=str(e))



class EODRequest(BaseModel):
    user_id: str
    activities: str

class EODResponse(BaseModel):
    content: str

@router.post("/", response_model=EODResponse)
async def generate_eod(data: EODRequest):
    try:
        prompt = (
            f"Generate a professional End Of Day (EOD) report based on these activities:\n\n"
            f"{data.activities.strip()}\n\n"
            "Include sections for Tasks Completed, Achievements, Next Steps, and Challenges."
        )
        content = get_gemini_response(prompt)
        return EODResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
