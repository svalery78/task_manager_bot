from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    text = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    remind_at = Column(DateTime, nullable=True)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime, nullable=True)

class Database:
    def __init__(self):
        self.engine = create_engine(Config.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
    
    def add_task(self, user_id: int, text: str, remind_at=None) -> int:
        """Добавляет новую задачу в базу данных"""
        session = self.Session()
        try:
            new_task = Task(
                user_id=user_id,
                text=text,
                remind_at=remind_at
            )
            session.add(new_task)
            session.commit()
            return new_task.id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

# Инициализация БД
db = Database()