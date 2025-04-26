from fastapi import APIRouter, HTTPException
from schemas.eod_schemas import EODRequest, EODResponse
from services.gemini_service import get_gemini_response
from services.qdrant_service import upsert_vector
import numpy as np  
router = APIRouter()



@router.post("/", response_model=EODResponse)
async def generate_eod(data: EODRequest):
    try:
        prompt = (
            f"Generate a concise End Of Day (EOD) report based on these activities:\n\n"
            f"{data.activities.strip()}\n\n"
            "Include only the most important points in a short and clear format. Limit the report to a few sentences, focusing on key tasks and outcomes."
        )
        content = get_gemini_response(prompt)

        dummy_vector = np.random.rand(1536).tolist()
        payload = {
            "user_id": data.user_id,
            "activities": data.activities,
            "eod_summary": content
        }
        upsert_vector(collection_name="eod_collection", vector=dummy_vector, payload=payload)

        return EODResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
