from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.performance import(
    PlayerPerformanceCreate, 
    PlayerPerformanceResponse,
    PlayerPerformanceUpdate
    )
from app.services.performance_service import (
    register_performance, 
    get_all_performances,
    get_performance,
    edit_performance,
    remove_performance
)

router = APIRouter()

@router.post("/performances", response_model=PlayerPerformanceResponse)
def create_performance_endpoint(
    performance: PlayerPerformanceCreate,
    db: Session = Depends(get_db),
): 
    return register_performance(db, performance)

@router.get("/performances", response_model=list[PlayerPerformanceResponse])
def get_performances(db: Session = Depends(get_db)):
    return get_all_performances(db)

@router.get("/performances/{performance_id}", response_model=PlayerPerformanceResponse)
def get_performance_endpoint(
    performance_id: int,
    db: Session = Depends(get_db)
): 
    return get_performance(db, performance_id)

@router.put("/performances/{performance_id}", response_model=PlayerPerformanceResponse)
def update_performance_endpoint(
    performance_id: int,
    performance_data: PlayerPerformanceUpdate,
    db: Session = Depends(get_db)
): 
    return edit_performance(db, performance_id, performance_data)

@router.delete("/performances/{performance+id}", response_model= PlayerPerformanceResponse)
def delete_performance_endpoint(
    performance_id: int,
    db: Session = Depends(get_db)
): 
    remove_performance(db, performance_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)