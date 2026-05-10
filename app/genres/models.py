from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True)
    games = relationship("Game",back_populates="genre")