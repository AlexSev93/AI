from flask import Flask, render_template,   request
from api_parser import country_id
app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello World!"
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
        name_vacansy = request.form['name_vacansy']
        name_country = request.form['name_country']

        print(country_id(name_country))
        return render_template('form.html')
        # return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)
