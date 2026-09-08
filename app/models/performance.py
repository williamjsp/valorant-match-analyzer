from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class PlayerPerformance(Base): 
    __tablename__ = "player_performances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    match_id: Mapped[str] = mapped_column(String, index=True)
    map: Mapped[str] = mapped_column(String)
    agent: Mapped[str] = mapped_column(String)
    kills: Mapped[int] = mapped_column(Integer)
    deaths: Mapped[int] = mapped_column(Integer)
    assists: Mapped[int] = mapped_column(Integer)
    result: Mapped[str] = mapped_column(String)
    