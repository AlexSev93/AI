from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///orm.sqlite', echo=True)
Session = sessionmaker(bind=engine)

session = Session()


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


# создание таблицы



Base.metadata.create_all(engine)


# запись одного
# myobject = Regions('foo')
# try:
#     session.add(myobject)
#     session.commit()
# except:
#     print('есть')

# запись много
# vacancies = [['111', 'qqq'], ['222', 'www'], ['333', 'eee']]
# vacancies = [Vacancies(vacancy[0], vacancy[1]) for vacancy in vacancies]
#
# session.add_all(vacancies)
# session.commit()

regions = ['111', '222', '333']
regions = [Regions(region) for region in regions]

session.add_all(regions)
session.commit()

# изменение объекта

# выборка
# request = session.query(Vacancies).all()
# print(request[0].region_name)
# for i, r in enumerate(request):
#     print(r)

# выборка с условием
# request = session.query(Vacancies).filter(Vacancies.region_name == 'www').all()
# print(request)

