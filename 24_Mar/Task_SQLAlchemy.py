from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import sqlite

Base = declarative_base()

class Task(Base):
    __tablename__ = "task"  # table name
    id = Column("id", Integer, primary_key=True)
    taskname = Column("taskname", String)
    description = Column("description", String)
    priority = Column("priority", Integer)

    def __init__(self, id, taskname, description, priority):
        self.id = id
        self.taskname = taskname
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"{self.id} --{self.taskname} --{self.description}--{self.priority}"



def poc():
    engine = create_engine("sqlite:///freak.db", echo=True)  # rituals
    Base.metadata.create_all(bind=engine)  # create tables
    Session = sessionmaker(bind=engine)  # create the class
    session = Session()  # object creation
    task=Task(3,"second Task","nothing",4)
    session.add(task)
    session.commit();

    results =session.query(Task).all()
    for r in results:
        print(r)

poc()



