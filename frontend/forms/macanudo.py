# -*- coding: utf-8 -*-
from flaskext.wtf import Form, TextField, IntegerField, SelectField, Required, Email, RecaptchaField

class MacanudoForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  habilidades = TextField('Tags')
  jornada = SelectField('Jornada', choices=[('100', 'Full-time'), ('200', 'Part-time')])
  lugar = TextField('Lugar', validators=[Required()])
  ocupacion = TextField('Ocupación', validators=[Required()])
  recaptcha = TextField('Ocupación')
  sueldo = IntegerField('Sueldo', validators=[Required()])
