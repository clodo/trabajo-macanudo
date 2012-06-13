# -*- coding: utf-8 -*-

import factory
from frontend.models import Macaundo, Tag
import random

class MacanudoFactory(factory.Factory):
  FACTORY_FOR = Macanudo

  email = factory.Sequence(lambda n: 'soyelnumero{0}'.format(n))
  jornada = random.choice([Macanudo.FULL_TIME, Macanudo.PART_TIME])
  ocupacion = random.choice(['Desarrollador Web Sr.', 'Project Manager', 'Gerente General', 'Más Capito'])
  sueldo = random.randrange(9000, 15000)
  lugar = random.choice(['Chacarita', 'Colegiales', 'Capital Federal', 'Centro', 'Zona norte'])
