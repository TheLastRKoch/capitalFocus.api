from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, engine


class Budget(Base):
    __tablename__ = "budget"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    date = Column(String)
    userID = Column(String)

    # Relationships
    sections = relationship("Section", back_populates="budget")


Base.metadata.create_all(engine,  checkfirst=True)
