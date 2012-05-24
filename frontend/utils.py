# -*- coding: utf-8 -*-

from datetime import datetime

def timesince(dt, default="hace un toque"):
  now = datetime.utcnow()
  diff = now - dt
    
  periods = (
    (diff.days / 365, "a&ntilde;o", "a&ntilde;os"),
    (diff.days / 30, "mes", "meses"),
    (diff.days / 7, "semana", "semanas"),
    (diff.days, "d&iacute;a", "d&iacute;as"),
    (diff.seconds / 3600, "hora", "horas"),
    (diff.seconds / 60, "minuto", "minutos"),
    (diff.seconds, "segundo", "segundos"),
  )

  for period, singular, plural in periods:
    if period:
      return "hace %d %s" % (period, singular if period == 1 else plural)

  return default