from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.babel import Babel

app = Flask(__name__)
app.config.from_object('config')

# Extensiones
db = SQLAlchemy(app)
# babel = Babel(app)

# Blueprints
from frontend.views import main
app.register_blueprint(main.mod)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404