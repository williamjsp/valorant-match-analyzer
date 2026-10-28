from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.metrics.performance_metrics import performances_creations_total

from app.models.performance import PlayerPerformance
from app.repositories.performance_repository import (
    create_performance,
    list_performances,
    get_performance_by_id,
    update_performance,
    delete_performance  
)
from app.schemas.performance import(
    PlayerPerformanceCreate,
    PlayerPerformanceUpdate
)

from app.mappers.performance_mapper import to_model

from app.observability.elk_logger import send_event

def register_performance(
    db: Session,
    performance_data: PlayerPerformanceCreate,
    ) -> PlayerPerformance:
    performance = to_model(performance_data)

    created_performance = create_performance(db, performance)

    performances_creations_total.inc()

    send_event(
        event="performance_created",
        performance_id=created_performance.id,
        request_method="POST",
        endpoint=f"/performances"
        )

    return created_performance

def get_all_performances(
    db: Session,
) -> list[PlayerPerformance]:
    return list_performances(db)

def get_performance(
    db: Session,
    performance_id: int
) -> PlayerPerformance:
    performance = get_performance_by_id(db, performance_id)

    if performance is None:
        raise HTTPException(status_code = 404, detail="Performance not found")
    return performance

def edit_performance(
    db: Session,
    performance_id: int,
    performance_data: PlayerPerformanceUpdate
) -> PlayerPerformance:
    performance = get_performance_by_id(db, performance_id)

    if performance is None:
        raise HTTPException(
            status_code = 404,
            detail="Performance not found"
        )

    performance.match_id = performance_data.match_id
    performance.map = performance_data.map
    performance.agent = performance_data.agent
    performance.kills = performance_data.kills
    performance.deaths = performance_data.deaths
    performance.assists = performance_data.assists
    performance.result = performance_data.result   

    updated_performance = update_performance(db, performance)

    send_event(
        event="performance_updated",
        performance_id=updated_performance.id,
        request_method="PUT",
        endpoint=f"/performances/{updated_performance.id}"
    )

    return updated_performance

def remove_performance(
    db: Session,
    performance_id: int
) -> None: 
    performance = get_performance_by_id(db, performance_id)

    if performance is None:
        raise HTTPException(
            status_code = 404,
            detail="Performance not found"
        )

    delete_performance(db, performance)

    send_event(
        event="performance_deleted",
        performance_id=performance.id,
        request_method="DELETE",
        endpoint=f"/performances/{performance.id}"
    )