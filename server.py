from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import autos
from flask_app.controllers import procesos


if __name__=="__main__":
    app.run(debug=True)