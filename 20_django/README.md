## Пользовательская команда ищет вакансии в регионе и заполняет базу.


### Модель базы

Regions:
  + region ---> unique

Keywords:
  + word ---> unique

Vacancy:
  + vacancy
  + regions ---> ForeignKey(Regions)
  + words ---> ManyToManyField(Keywords)


### Использование
  - Ввод команды: python manege.py fill_db <название региона> <название вакансиии>
  - В названии вакансии вместо пробелов использовать .
