from flask import Flask, render_template, url_for
from features.steps.storage import Storage

app = Flask(__name__)


@app.route('/')
def report_page():
    return render_template("index.html")

@app.route('/scenario1')
def scenario1_page():
    company_filter = Storage.company_list
    percent= Storage.company_from_ui_percent_increase
    price= Storage.company_from_ui_price
    return render_template("scenario1.html", company=company_filter, price = price, percent=percent, num=len(company_filter)+1)

@app.route('/scenario2')
def scenario2_page():
    company_filter = Storage.company_list
    dividends = Storage.dividends
    return render_template("scenario2.html", company=company_filter, dividends=dividends, num=len(company_filter)+1)

@app.route('/scenario3')
def scenario3_page():
    return render_template("scenario3.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
