from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.utils.database import Base

class Table(Base):
    __tablename__ = "Table"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    test_id = Column(Integer, ForeignKey('Test.id'))
    date_created = Column(DateTime, default=datetime.utcnow())
    date_updated = Column(DateTime, default=datetime.utcnow())

    test = relationship("Test", back_populates="tables")
