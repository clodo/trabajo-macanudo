from frontend.extensions import db
from datetime import datetime

class Postulacion(db.Model):
  FULL_TIME = 100
  PART_TIME = 200
  
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  #ocupacion_actual = db.Column(db.String(120))
  #sueldo_actual = db.Column(db.Integer)
  #area_actual = db.Column(db.String(120))
  carga_horaria_pretendida = db.Column(db.Integer, default=FULL_TIME)
  ocupacion_pretendida = db.Column(db.String(120))
  sueldo_pretendido = db.Column(db.Integer)
  lugar_pretendido = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime(), default=datetime.utcnow)

  def __init__(self, *args, **kwargs):
    super(Postulacion, self).__init__(*args, **kwargs)

  def get_pub_date(self):
    return self.pub_date

  def __repr__(self):
    return 'Quiero trabajar de <b>{que}</b> de forma <b>{como}</b> en la zona de <b>{donde}</b> y quiero ganar <b>{cuanto}<b>.'.format(que=self.ocupacion_pretendida, cuanto=self.sueldo_pretendido, donde=self.lugar_pretendido, como=self.carga_horaria_pretendida)
