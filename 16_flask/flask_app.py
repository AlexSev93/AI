from flask import Flask, render_template, request, jsonify
from api_parser import get_vacansies_id, get_keywords, get_country_id, get_better_vacanci
import json
import pprint

app = Flask(__name__)

@app.route("/")
def index():
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

        country_id = get_country_id(name_request)

        vacansies_id = get_vacansies_id(country_id, name_request)

        vacancies_keywords, vacancies_info = get_keywords(vacansies_id)

        better_vacanci = get_better_vacanci(vacancies_keywords, vacancies_info)
        links = [link for link in better_vacanci[0]]
        name_vacansy = [link for link in better_vacanci[1]]
        description = [link for link in better_vacanci[2]]
        #write_to_json(name_vacansy, vacansies_id, vacancies_keywords)
        #return render_template('form.html')
        return render_template('contacts.html', name_request=name_request, name_country=name_country,
                               count_vacansies=len(vacansies_id), better_vacanci=better_vacanci)


if __name__ == "__main__":
    app.run(debug=True)
