from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from src.utils.database import Base

class Test(Base):
    __tablename__ = "Test"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    date_updated = Column(DateTime, default=datetime.utcnow())

    tables = relationship("Table", back_populates="test") # one to many