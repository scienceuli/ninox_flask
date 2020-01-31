from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/mitglieder')
def mitglieder():
    headers = {"Authorization":"Bearer 5a3a3430-a6b7-11e8-833a-c390db8727db"}
    endpoint = 'https://api.ninoxdb.de/v1/teams/g7DEtaLSmfv2pByid/databases/uyvkcqihm64r/tables/E/records'
    mitglieder = requests.get(endpoint, headers=headers).json()
    return render_template('mitglieder.html', title = 'Mitglieder', mitglieder = mitglieder)

@app.route('/projekte')
def projekte():
    headers = {"Authorization":"Bearer 5a3a3430-a6b7-11e8-833a-c390db8727db"}
    endpoint = 'https://api.ninoxdb.de/v1/teams/g7DEtaLSmfv2pByid/databases/uyvkcqihm64r/tables/A/records'
    projekte = requests.get(endpoint, headers=headers).json()
    return render_template('projekte.html', title = 'Projekte', projekte = projekte)


if __name__ == '__main__':
    app.run(debug=True)



