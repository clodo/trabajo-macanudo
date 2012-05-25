# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request
from frontend.models import Postulacion, Tag
from frontend.forms import PostulacionForm
from frontend.extensions import db

mod = Blueprint('main', __name__)

@mod.route('/', methods=("GET", "POST"))
def home():
  form = PostulacionForm()
  if form.validate_on_submit():
    postulacion = Postulacion()
    form.populate_obj(postulacion)

    for tag in form.capacidades.data.split(','):
      tag_name = tag.strip()
      t = Tag.query.filter_by(name=tag_name).first() or Tag(tag_name)
      postulacion.tags.append(t)

    db.session.add(postulacion)
    db.session.commit()

    flash("Success")

    return redirect(url_for('main.home'))
  
  return render_template('main/home.html', form=form)

@mod.route("/buscados")
@mod.route("/buscados/<int:page>/")
def buscados(page=1):
  postulaciones = Postulacion.query.order_by(Postulacion.pub_date.desc()).paginate(page, 20)
  return render_template('main/buscados.html', postulaciones=postulaciones)

@mod.route("/ofrecidos")
def ofrecidos():
  return render_template('main/ofrecidos.html')

@mod.route("/contacto")
def contacto():
  return render_template('main/contacto.html')

@mod.route("/acerca-de")
def acercade():
  return render_template('main/acercade.html')