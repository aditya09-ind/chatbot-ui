from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# Create DB
engine = create_engine("sqlite:///chat.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"  

    id = Column(Integer, primary_key=True, index=True)
    chat_name = Column(String)
    role = Column(String)
    content = Column(Text)

# Create table
Base.metadata.create_all(engine)
