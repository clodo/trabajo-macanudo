from flask import Blueprint, render_template
from frontend.models import Postulacion

mod = Blueprint('main', __name__)

@mod.route('/')
def home():
  return render_template('main/home.html')

@mod.route('/ofrecidos')
def ofrecidos():
  postulaciones = Postulacion.query.all()
  return render_template('main/ofrecidos.html', postulaciones=postulaciones)