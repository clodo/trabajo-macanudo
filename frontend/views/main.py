# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for
from frontend.models import Postulacion
from frontend.forms import PostulacionForm

mod = Blueprint('main', __name__)

@mod.route('/', methods=("GET", "POST"))
def home():
  form = PostulacionForm()
  if form.validate_on_submit():
    flash("Success")
    return redirect(url_for('main.home'))
  
  return render_template('main/home.html', form=form)

@mod.route('/ofrecidos')
def ofrecidos():
  postulaciones = Postulacion.query.all()
  return render_template('main/ofrecidos.html', postulaciones=postulaciones)