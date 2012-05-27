# -*- coding: utf-8 -*-
from flaskext.wtf import Form, TextField, IntegerField, SelectField, Required, Email, RecaptchaField

class EmpleoForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  jornada = SelectField('Jornada', choices=[('100', 'Full-time'), ('200', 'Part-time')])
  ocupacion = TextField('Ocupación', validators=[Required()])
  sueldo = IntegerField('Sueldo', validators=[Required()])
  lugar = TextField('Lugar', validators=[Required()])
  habilidades = TextField('Tags')
  recaptcha = RecaptchaField()