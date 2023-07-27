from flask import Flask, render_template, request
from api_parser import get_vacansies_id, get_keywords, get_country_id, get_better_vacanci
from sql import def_for_parser_db as def_db
from orm import orm

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        remove_status = request.form['remove_data']
        if remove_status:
            def_db.remove_data()
        return render_template('index.html')


@app.route("/contacts/")
def contacts():
    return render_template('contacts.html')


@app.route("/form/", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name_request = request.form['name_vacansy']
        name_country = request.form['name_country']

        pages = int(request.form['pages_radio'].replace('value_', ''))

        country_id = get_country_id(name_request)
        vacansies_id = get_vacansies_id(country_id, name_request, pages)
        vacancies_keywords, vacancies_info = get_keywords(vacansies_id)
        better_vacanci = get_better_vacanci(vacancies_keywords, vacancies_info)

        value, keywords = [vacancies_keywords[key] for key in vacancies_keywords.keys()], \
                          [key for key in vacancies_keywords.keys()]

        orm.insert_request_info(name_country, name_request, vacancies_keywords)

        return render_template('contacts.html', name_request=name_request, name_country=name_country,
                               count_vacansies=len(vacansies_id), better_vacanci=better_vacanci,
                               value=value, keywords=keywords)


if __name__ == "__main__":
    app.run(debug=True)
