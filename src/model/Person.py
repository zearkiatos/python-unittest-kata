import datetime
from src.Community.base import Session, engine, Base
from sqlalchemy import Column, Integer, String


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)

    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year

    def set_year(self, year) -> None:
        self.year = year

    def set_name(self, name) -> None:
        self.name = name

    def get_year(self) -> int:
        return self.year

    def get_name(self) -> str:
        return self.name

    def calculate_birth_day(self, already_complete_year) -> int:
        current_year = datetime.datetime.now().year
        if already_complete_year:
            return current_year - self.year
        else:
            return current_year - self.year + 1

    def store(self) -> None:
        Base.metadata.create_all(engine)
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    def find(self, name, year) -> None:
        session = Session()
        person = session.query(Person).filter(
            Person.name == name and Person.year == year).first()
        session.close()
        self.name = person.name
        self.year = person.year
        self.id = person.id
