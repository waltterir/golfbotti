from pydantic import BaseModel, Field

# --- Sisään ---
class HourlyWeather(BaseModel):
    hour: int = Field(ge=0, le=23)
    wind: float = Field(ge=0, allow_inf_nan=False)
    temp: float = Field(ge=-60, le=40, allow_inf_nan=False)
    rain: float = Field(ge=0, allow_inf_nan=False)

class GolfIndexRequest(BaseModel):
    hours: list[HourlyWeather]

# --- Ulos ---
class GolfIndexResponse(BaseModel):
    best: str | None
    windows: dict[str, float]