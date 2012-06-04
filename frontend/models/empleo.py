from frontend.extensions import db
from datetime import datetime

tags = db.Table('tags',
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
  db.Column('empleo_id', db.Integer, db.ForeignKey('empleo.id'))
)

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)

  empleos = db.relationship('Empleo', secondary=tags, backref=db.backref('tags', lazy='joined'))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

class Empleo(db.Model):
  FULL_TIME = 100
  PART_TIME = 200

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  jornada = db.Column(db.Integer)
  ocupacion = db.Column(db.String(120))
  sueldo = db.Column(db.Integer)
  lugar = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  #tags = db.relationship('Tag', secondary=tags, backref=db.backref('empleos', lazy='joined'))

  def __init__(self, *args, **kwargs):
    super(Empleo, self).__init__(*args, **kwargs)

  def __repr__(self):
    return email

  def get_jornada(self):
    return 'Full-time' if self.jornada == self.FULL_TIME else 'Part-time'