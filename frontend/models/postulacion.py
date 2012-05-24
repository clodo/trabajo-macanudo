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
  #ocupacion_actual = db.Column(db.String(120))
  #sueldo_actual = db.Column(db.Integer)
  #area_actual = db.Column(db.String(120))
  tipo_pretendido = db.Column(db.Integer, default=FULL_TIME)
  ocupacion_pretendida = db.Column(db.String(120))
  sueldo_pretendido = db.Column(db.Integer)
  lugar_pretendido = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  tags = db.relationship('Tag', secondary=tags, backref=db.backref('postulaciones', lazy='dynamic'))

  def __init__(self, *args, **kwargs):
    super(Postulacion, self).__init__(*args, **kwargs)

  def __repr__(self):
    return 'Quiero trabajar <b>{tipo}</b> como <b>{como}</b> en la zona de <b>{donde}</b> y ganar <b>{cuanto}</b> pesos por mes.'.format(como=self.ocupacion_pretendida, cuanto=self.sueldo_pretendido, donde=self.lugar_pretendido, tipo=self.get_tipo())

  def get_pub_date(self):
    return self.pub_date

  def get_tipo(self):
    return 'Full-time' if self.tipo_pretendido == self.FULL_TIME else 'Part-time'

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)

  def __init__(self, *args, **kwargs):
    super(Tag, self).__init__(*args, **kwargs)

  def __repr__(self):
    return self.name
