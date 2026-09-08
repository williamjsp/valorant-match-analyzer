from app.models.performance import PlayerPerformance
from app.schemas.performance import PlayerPerformanceCreate

def to_model(
    performance_data: PlayerPerformanceCreate
    ) -> PlayerPerformance:
    return PlayerPerformance(**performance_data.model_dump())

