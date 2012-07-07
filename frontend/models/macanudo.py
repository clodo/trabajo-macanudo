from frontend.extensions import db
from datetime import datetime

macanudo_tags = db.Table('macanudo_tags',
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
  db.Column('macanudo_id', db.Integer, db.ForeignKey('macanudo.id'))
)

trabajo_macanudo_tags = db.Table('trabajo_macanudo_tags',
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
  db.Column('trabajo_macanudo_id', db.Integer, db.ForeignKey('trabajo_macanudo.id'))
)

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)

  macanudos = db.relationship('Macanudo', secondary=macanudo_tags, backref=db.backref('tags', lazy='joined'))
  trabajos_macanudos = db.relationship('TrabajoMacanudo', secondary=trabajo_macanudo_tags, 
                                       backref=db.backref('tags', lazy='joined'))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

class Macanudo(db.Model):
  FULL_TIME = 100
  PART_TIME = 200

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  jornada = db.Column(db.Integer)
  ocupacion = db.Column(db.String(120))
  sueldo = db.Column(db.Integer)
  lugar = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  #tags = db.relationship('Tag', secondary=tags, backref=db.backref('macanudos', lazy='joined'))

  def __init__(self, *args, **kwargs):
    super(Macanudo, self).__init__(*args, **kwargs)

  def __repr__(self):
    return pub_date

  def get_jornada(self):
    return 'Full-time' if self.jornada == self.FULL_TIME else 'Part-time'

class TrabajoMacanudo(db.Model):
  EXPERIENCIAS = ('mucha experiencia', 
                  'media experencia', 
                  'poca experencia', 
                  'ganas de aprender')

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  experiencia = db.Column(db.Integer)
  ocupacion = db.Column(db.String(120))
  sobre_la_empresa = db.Column(db.Text)
  sobre_el_puesto = db.Column(db.Text)
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  def __init__(self, *args, **kwargs):
    super(TrabajoMacanudo, self).__init__(*args, **kwargs)

  def __repr__(self):
    return pub_date

  def get_jornada(self):
    return self.EXPERIENCIAS[self.experiencia]
