from frontend.extensions import db
from datetime import datetime

tags = db.Table('tags',
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
  db.Column('postulacion_id', db.Integer, db.ForeignKey('postulacion.id'))
)

class Postulacion(db.Model):
  FULL_TIME = 100
  PART_TIME = 200

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  jornada = db.Column(db.Integer)
  ocupacion = db.Column(db.String(120))
  sueldo = db.Column(db.Integer)
  lugar = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  tags = db.relationship('Tag', secondary=tags, backref=db.backref('postulaciones', lazy='dynamic'))

  def __init__(self, *args, **kwargs):
    super(Postulacion, self).__init__(*args, **kwargs)

  def __repr__(self):
    return email

  def get_pub_date(self):
    return self.pub_date

  def get_jornada(self):
    return 'Full-time' if self.jornada == self.FULL_TIME else 'Part-time'

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name
