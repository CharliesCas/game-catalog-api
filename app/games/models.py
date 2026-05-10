from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone

def nowutc():
    return datetime.now(timezone.utc)

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),index=True)
    release_year = Column(Integer,index=True)
    platform = Column(String(255),index=True)
    genre_id = Column(Integer,ForeignKey("genres.id"))
    genre = relationship("Genre",back_populates="games")
    created_at = Column(DateTime,default=nowutc)

