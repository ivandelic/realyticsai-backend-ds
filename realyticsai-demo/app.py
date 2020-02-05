from flask import Flask, send_file, request
from realestateanalyzer import RealestateAnalyzer

app = Flask(__name__)

@app.route("/")
def home():
    lgu = request.args.get('lgu')
    ra = RealestateAnalyzer("data-source/source-realestate-transactions.csv", "Year", "Transactions")
    byts = ra.analyze("JLS", lgu)
    return send_file(byts, attachment_filename='plot.png', mimetype='image/png')