from flask import Flask, render_template, url_for

from features.steps.parse_methods import dict_dividends
from features.steps.storage import Storage

app = Flask(__name__)


@app.route('/')
def report_page():
    return render_template("index.html")

@app.route('/scenario1')
def scenario1_page():
    return render_template("scenario1.html")

@app.route('/scenario2')
def scenario2_page():
    company_filter = Storage.company_from_base
    #company_filter = dict_dividends.keys()
    #company_dividends = dict_dividends.values()
    return render_template("scenario2.html", company=company_filter) #dividends=company_dividends

@app.route('/scenario3')
def scenario3_page():
    return render_template("scenario3.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
