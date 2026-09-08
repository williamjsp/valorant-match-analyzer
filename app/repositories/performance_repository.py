from sqlalchemy.orm import Session

from app.models.performance import PlayerPerformance

def create_performance(
    db:Session,
    performance: PlayerPerformance,
) -> PlayerPerformance: 
    try:
        db.add(performance)
        db.commit()
        db.refresh(performance)

        return performance
    except Exception:
         db.rollback()
         raise
    
def list_performances(
    db: Session
) -> list[PlayerPerformance]: 
    return db.query(PlayerPerformance).all()

def get_performance_by_id(
    db: Session,
    performance_id: int
) -> PlayerPerformance | None:
    return (
        db.query(PlayerPerformance).filter(
        PlayerPerformance.id == performance_id).first()
    )

def update_performance(
    db: Session,
    performance: PlayerPerformance
    ) -> PlayerPerformance:
        try:
            db.commit()
            db.refresh(performance)
        
            return performance
        except Exception:
             db.rollback()
             raise

def delete_performance(
    db: Session,
    performance: PlayerPerformance
) -> None:
    try: 
        db.delete(performance)
        db.commit()
    except Exception:
         db.rollback()
         raise