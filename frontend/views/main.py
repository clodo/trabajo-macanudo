# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from frontend.models import Macanudo, Tag, TrabajoMacanudo
from frontend.forms import MacanudoForm, TrabajoMacanudoForm
from frontend.extensions import db
from frontend.utils import normalizar_tags
import twitter

mod = Blueprint('main', __name__)

@mod.route('/', methods=("GET", "POST"))
def home():
  form = MacanudoForm()
  if form.validate_on_submit():
    macanudo = Macanudo()
    form.populate_obj(macanudo)

    for tag_name in normalizar_tags(form.habilidades.data):
      t = Tag.query.filter_by(name=tag_name).first() or Tag(tag_name)
      macanudo.tags.append(t)

    db.session.add(macanudo)
    db.session.commit()

    twitter_api = twitter.Api(
      consumer_key=current_app.config['TWITTER_CONSUMER_KEY'],
      consumer_secret=current_app.config['TWITTER_CONSUMER_SECRET'],
      access_token_key=current_app.config['TWITTER_TOKEN'],
      access_token_secret=current_app.config['TWITTER_SECRET']
    )

    twitter_status = '%(ocupacion)s %(jornada)s en la zona de %(lugar)s por %(sueldo)s pesos al mes %(base_url)s' % \
      { "jornada": macanudo.get_jornada(), "ocupacion": macanudo.ocupacion, "lugar": macanudo.lugar, "sueldo": macanudo.sueldo, "base_url": "http://www.trabajomacanudo.com.ar" }

    #try:
    #  twitter_api.PostUpdate(twitter_status)
    #except:
    #  pass

    flash("Success")

    return redirect(url_for('main.home'))

  macanudos = Macanudo.query.order_by(Macanudo.pub_date.desc()).limit(6)

  return render_template('main/home.html', form=form, macanudos=macanudos)

@mod.route("/ofrecidos/")
@mod.route("/ofrecidos/<int:page>")
def ofrecidos(page=1):
  filter_tags = normalizar_tags(request.args.get('tags') or '')
  
  macanudos_query = Macanudo.query.order_by(Macanudo.pub_date.desc())
  
  if len(filter_tags) > 0:
    macanudos_query = macanudos_query.join(Macanudo.tags).filter(Tag.name.in_(filter_tags))

  macanudos = macanudos_query.paginate(page, 20)

  #macanudos = Macanudo.query.join(Macanudo.tags).filter(Tag.name.in_(tags)).order_by(Macanudo.pub_date.desc()).paginate(page, 20)
  return render_template('main/ofrecidos.html', macanudos=macanudos)

@mod.route("/ofrecer-trabajo-macanudo/", methods=("GET", "POST"))
def ofrecer_trabajo_macanudo():
  form = TrabajoMacanudoForm()
  if form.validate_on_submit():
    trabajo_macanudo = TrabajoMacanudo()
    form.populate_obj(trabajo_macanudo)

    for tag_name in normalizar_tags(form.habilidades.data):
      t = Tag.query.filter_by(name=tag_name).first() or Tag(tag_name)
      trabajo_macanudo.tags.append(t)

    db.session.add(trabajo_macanudo)
    db.session.commit()

    flash("Success")
    return redirect(url_for('main.ofrecidos'))

  return render_template('main/ofrecer.html', form = form)

@mod.route("/buscados/")
def buscados():
  return render_template('main/buscados.html')

@mod.route("/contacto/")
def contacto():
  return render_template('main/contacto.html')

@mod.route("/acercade/")
def acercade():
  return render_template('main/acercade.html')
