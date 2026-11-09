from fastapi import FastAPI
from app.schemas.schemas import GolfIndexRequest, GolfIndexResponse
from app.golf_index import best_window

# --- App ---
app = FastAPI()

# --- Get Health---
@app.get("/health")
def get_health():
    return {"status": "ok"}

# --- Post indexi --- 
@app.post("/golf-index", response_model=GolfIndexResponse)
def calculate_golfindex(request: GolfIndexRequest):
    hour_list = [r.model_dump() for r in request.hours]
    result = best_window(hour_list)
    return result
