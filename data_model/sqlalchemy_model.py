from sqlalchemy import Column, String, Integer, TIMESTAMP,  ForeignKey
from sqlalchemy.sql.expression import text
from  connection.posgresql import Base

class Continent(Base):
    __tablename__ = "continent"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    
class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    continent_id = Column(Integer, ForeignKey('continent.id'))
    
class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    country_id = Column(Integer, ForeignKey('country.id'))
    
class LocalGovt(Base):
    __tablename__ = "local_govt"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    states_id = Column(Integer, ForeignKey('states.id'))