from frontend import db
from datetime import datetime

class Postulacion(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  ocupacion_actual = db.Column(db.String(120))
  sueldo_actual = db.Column(db.Float())
  area_actual = db.Column(db.String(120))
  pub_date = db.Column(db.DateTime())

  def __init__(self, email, ocupacion_actual, sueldo_actual, area_actual):
    self.email = email
    self.ocupacion_actual = ocupacion_actual
    self.sueldo_actual = sueldo_actual
    self.area_actual = area_actual
    self.pub_date = datetime.now()

  def __repr__(self):
    return self.email