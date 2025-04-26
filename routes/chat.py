from fastapi import APIRouter, HTTPException
from schemas.chat_schemas import ChatResponse, ChatRequest
from services.gemini_service import get_gemini_response
from services.qdrant_service import upsert_vector
import numpy as np 
    
router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_with_ai(data: ChatRequest):
    try:
        reply = get_gemini_response(data.message)

        dummy_vector = np.random.rand(1536).tolist() 
        payload = {
            "user_id": data.user_id,
            "message": data.message,
            "reply": reply,
        }
        upsert_vector(collection_name="chat_collection", vector=dummy_vector, payload=payload)

        return ChatResponse(role="assistant", content=reply)
    except Exception as e:
        print("❌ Gemini ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
