# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from frontend.models import Empleo, Tag
from frontend.forms import EmpleoForm
from frontend.extensions import db
from frontend.utils import normalizar_tags
#import twitter

mod = Blueprint('main', __name__)

@mod.route('/', methods=("GET", "POST"))
def home():
  form = EmpleoForm()
  if form.validate_on_submit():
    empleo = Empleo()
    form.populate_obj(empleo)

    for tag_name in normalizar_tags(form.habilidades.data):
      t = Tag.query.filter_by(name=tag_name).first() or Tag(tag_name)
      empleo.tags.append(t)

    db.session.add(empleo)
    db.session.commit()

    twitter_api = twitter.api(
      consumer_key=current_app.config['TWITTER_CONSUMER_KEY'],
      consumer_secret=current_app.config['TWITTER_CONSULER_SECRET'],
      access_token_key=current_app.config['TWITTER_TOKEN'],
      access_token_secret=current_app.config['TWITTER_SECRET']
    )

    flash("Success")

    return redirect(url_for('main.home'))

  return render_template('main/home.html', form=form)

@mod.route("/buscados/")
@mod.route("/buscados/<int:page>")
def buscados(page=1):
  filter_tags = normalizar_tags(request.args.get('tags') or '')
  
  empleos_query = Empleo.query.order_by(Empleo.pub_date.desc())
  
  if len(filter_tags) > 0:
    empleos_query = empleos_query.join(Empleo.tags).filter(Tag.name.in_(filter_tags))

  empleos = empleos_query.paginate(page, 20)

  #empleos = Empleo.query.join(Empleo.tags).filter(Tag.name.in_(tags)).order_by(Empleo.pub_date.desc()).paginate(page, 20)
  return render_template('main/buscados.html', empleos=empleos)

@mod.route("/ofrecidos/")
def ofrecidos():
  return render_template('main/ofrecidos.html')

@mod.route("/contacto/")
def contacto():
  return render_template('main/contacto.html')

@mod.route("/acerca-de/")
def acercade():
  return render_template('main/acercade.html')
