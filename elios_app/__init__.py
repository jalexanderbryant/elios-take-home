from flask import Flask
app = Flask(__name__)
import elios_app.views

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)