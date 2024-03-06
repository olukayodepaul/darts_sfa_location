"""
Module representing SQLAlchemy models for geographic data.
"""

from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.sql.expression import text
from connection.posgresql import Base
from sqlalchemy.orm import relationship

class Continent(Base):
    """
    Model representing a continent.
    """
    __tablename__ = "continent"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    countries = relationship("Country", back_populates="continent")

class Country(Base):
    """
    Model representing a country.
    """
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    continent_id = Column(Integer, ForeignKey('continent.id'))
    continent = relationship("Continent", back_populates="countries")

class State(Base):
    """
    Model representing a state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship("Country")

class LocalGovt(Base):
    """
    Model representing a local government.
    """
    __tablename__ = "local_govt"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")
