from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///C:/Users/Admin/PycharmProjects/AI/18_orm/orm/orm.sqlite', echo=True)
Base = declarative_base()


class Regions(Base):
    __tablename__ = 'regions'
    key = Column(Integer, primary_key=True)
    region = Column(String, unique=True)

    def __init__(self, region):
        self.region = region

    def __repr__(self):
        return "<Regions('%s')>" % self.region

    def __str__(self):
        return f'{self.region}'


class Keywords(Base):
    __tablename__ = 'key_words'
    key = Column(Integer, primary_key=True)
    word = Column(String, unique=True)

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return "<Keywords('%s')>" % self.word

    def __str__(self):
        return f'{self.word}'


class Vacancies(Base):
    __tablename__ = 'vacancies'
    key = Column(Integer, primary_key=True)
    vacancy = Column(String)
    region_name = Column(String, ForeignKey('regions.region'))

    def __init__(self, vacancy, region_name):
        self.vacancy = vacancy
        self.region_name = region_name

    def __repr__(self):
        return "<Vacancies('%s', '%s')>" % (self.vacancy, self.region_name)


class VacanciesKeywords(Base):
    __tablename__ = 'vacancies_key_words'
    key = Column(Integer, primary_key=True)
    word = Column(String, ForeignKey('key_words.word'))
    vacancy = Column(String, ForeignKey('vacancies.vacancy'))

    def __init__(self, vacancy, word):
        self.vacancy = vacancy
        self.word = word

    def __repr__(self):
        return "<VacanciesKeywords('%s', '%s')>" % (self.vacancy, self.word)


if not os.path.exists('C:/Users/Admin/PycharmProjects/AI/18_orm/orm/orm.sqlite'):
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def insert_request_info(country, vacancy, key_words):
    regions_db = session.query(Regions).all()
    regions_db = [str(region) for region in regions_db]
    if country not in regions_db:
        new_region = Regions(country)
        session.add(new_region)
    session.commit()

    new_vacancy = Vacancies(vacancy, country)
    session.add(new_vacancy)
    session.commit()

    key_words_db = session.query(Keywords).all()
    key_words_db = [str(word) for word in key_words_db]
    for word in key_words:
        if word not in key_words_db:
            new_word = Keywords(word)
            session.add(new_word)
        new_vac_word = VacanciesKeywords(word, vacancy)
        session.add(new_vac_word)
        session.commit()

