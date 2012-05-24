# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request
from frontend.models import Postulacion
from frontend.forms import PostulacionForm
from frontend.extensions import db

mod = Blueprint('main', __name__)

@mod.route('/', methods=("GET", "POST"))
def home():
  form = PostulacionForm()
  if form.validate_on_submit():
    postulacion = Postulacion()
    form.populate_obj(postulacion)

    db.session.add(postulacion)
    db.session.commit()

    flash("Success")

    return redirect(url_for('main.home'))
  
  return render_template('main/home.html', form=form)

@mod.route('/ofrecidos')
def ofrecidos():
  postulaciones = Postulacion.query.order_by(Postulacion.pub_date.desc())
  return render_template('main/ofrecidos.html', postulaciones=postulaciones)