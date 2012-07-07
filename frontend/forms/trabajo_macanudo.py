# -*- coding: utf-8 -*-
from flaskext.wtf import Form, TextField, TextAreaField,IntegerField, SelectField, Required, Email, RecaptchaField

class TrabajoMacanudoForm(Form):
  email = TextField('Email', validators=[Required(), Email()])
  experiencia = SelectField('Experiencia', choices=[('0', 'mucha experiencia'), 
                                                    ('1', 'media experencia'), 
                                                    ('2', 'poca experencia'), 
                                                    ('3', 'ganas de aprender')])
  habilidades = TextField('Tags', validators=[Required()])
  ocupacion = TextField('Ocupación', validators=[Required()])
  recaptcha = RecaptchaField()
  sobre_la_empresa = TextAreaField('Sobre la Empresa', validators=[Required()])
  sobre_el_puesto = TextAreaField('Sobre el puesto', validators=[Required()])
