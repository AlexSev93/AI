from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


class Regions(Base):
    __tablename__ = 'regions'
    key = Column(Integer, primary_key=True)
    region = Column(String, unique=True)

    def __init__(self, region):
        self.region = region

    def __repr__(self):
        return "<Regions('%s')>" % self.region


class Keywords(Base):
    __tablename__ = 'key_words'
    key = Column(Integer, primary_key=True)
    word = Column(String, unique=True)

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return "<Keywords('%s')>" % self.word


class Vacancies(Base):
    __tablename__ = 'vacancies'
    key = Column(Integer, primary_key=True)
    vacancy = Column(String)
    word = Column(String)

    def __init__(self, vacancy, word):
        self.vacancy = vacancy
        self.word = word

    def __repr__(self):
        return "<Vacancies('%s', '%s')>" % (self.vacancy, self.word)


class VacanciesKeywords(Base):
    __tablename__ = 'vacancies_key_words'
    key = Column(Integer, primary_key=True)
    vacancy = Column(String)
    word = Column(String)

    def __init__(self, vacancy, word):
        self.vacancy = vacancy
        self.word = word

    def __repr__(self):
        return "<VacanciesKeywords('%s', '%s')>" % (self.vacancy, self.word)


# создание таблицы
Base.metadata.create_all(engine)