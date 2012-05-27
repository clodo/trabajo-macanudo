# -*- coding: utf-8 -*-

import factory
from frontend.models import Empleo, Tag
import random

class EmpleoFactory(factory.Factory):
  FACTORY_FOR = Empleo

  email = factory.Sequence(lambda n: 'soyelnumero{0}'.format(n))
  jornada = random.choice([Empleo.FULL_TIME, Empleo.PART_TIME])
  ocupacion = random.choice(['Desarrollador Web Sr.', 'Project Manager', 'Gerente General', 'Más Capito'])
  sueldo = random.randrange(9000, 15000)
  lugar = random.choice(['Chacarita', 'Colegiales', 'Capital Federal', 'Centro', 'Zona norte'])