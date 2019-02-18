from flask import Flask
from flask_cors import CORS
app = Flask(__name__, template_folder='static/public')
CORS(app)
import elios_app.views
import elios_app.models

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
