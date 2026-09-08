from pydantic import BaseModel, ConfigDict

class PlayerPerformanceCreate(BaseModel): 
    match_id: str
    map: str
    agent: str
    kills: int
    deaths: int
    assists: int
    result: str

class PlayerPerformanceResponse(PlayerPerformanceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class PlayerPerformanceUpdate(BaseModel): 
    match_id: str
    map: str
    agent: str
    kills: int
    deaths: int
    assists: int
    result: str