# -*- coding: utf-8 -*-

from flaskext.wtf import Form, TextField, IntegerField, SelectField, Required, Email

class PostulacionForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  # ocupacion_actual = TextField('Ocupación actual', validators=[Required()])
  # sueldo_actual = IntegerField('Sueldo actual', validators=[Required()])
  # area_actual = TextField('Area actual', validators=[Required()])
  tipo_pretendido = SelectField('Tipo de trabajo pretendido', choices=[('100', 'Full-time'), ('200', 'Part-time')])
  ocupacion_pretendida = TextField('Ocupación pretendida', validators=[Required()])
  sueldo_pretendido = IntegerField('Sueldo pretendido', validators=[Required()])
  lugar_pretendido = TextField('Lugar pretendido', validators=[Required()])
  capacidades = TextField('Tags')