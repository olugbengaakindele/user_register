from database import Base
from sqlalchemy import Column, Integer, String, Boolean 

class Students(Base):
    __tablename__ = 'students'

    user_id = Column(Integer,primary_key =True, index = True)
    name = Column(String)
    city = Column(String)
    country = Column(String)
    age = Column(Integer)
    uni = Column(String)
