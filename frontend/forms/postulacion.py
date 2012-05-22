# -*- coding: utf-8 -*-

from flaskext.wtf import Form, TextField, IntegerField, Required, Email

class PostulacionForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  ocupacion_actual = TextField('Ocupación actual', validators=[Required()])
  sueldo_actual = IntegerField('Sueldo actual', validators=[Required()])
  area_actual = TextField('Area actual', validators=[Required()])