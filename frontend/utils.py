# -*- coding: utf-8 -*-

from datetime import datetime

def timesince(dt, default=u'Recién'):
  now = datetime.utcnow()
  diff = now - dt
    
  periods = (
    (diff.days / 365, u'año', u'años'),
    (diff.days / 30, u'mes', u'meses'),
    (diff.days / 7, u'semana', u'semanas'),
    (diff.days, u'día', u'días'),
    (diff.seconds / 3600, u'hora', u'horas'),
    (diff.seconds / 60, u'minuto', u'minutos'),
    (diff.seconds, u'segundo', u'segundos'),
  )

  for period, singular, plural in periods:
    if period:
      return "Hace %d %s" % (period, singular if period == 1 else plural)

  return default

def normalizar_tags(tags='', separador=','):
  return set([tag.strip() for tag in tags.split(separador) if tag.strip()])
