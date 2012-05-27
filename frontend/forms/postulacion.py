# -*- coding: utf-8 -*-
from frontend.models import Postulacion
from flaskext.wtf import Form, TextField, IntegerField, SelectField, Required, Email, RecaptchaField

class PostulacionForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  jornada = SelectField('Tipo de trabajo pretendido', choices=[('100', 'Full-time'), ('200', 'Part-time')])
  ocupacion = TextField('Ocupación pretendida', validators=[Required()])
  sueldo = IntegerField('Sueldo pretendido', validators=[Required()])
  lugar = TextField('Lugar pretendido', validators=[Required()])
  habilidades = TextField('Tags')
  recaptcha = RecaptchaField()