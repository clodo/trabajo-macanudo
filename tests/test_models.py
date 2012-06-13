import factories
from frontend.models import Macanudo, Tag
from frontend.extensions import db
from tests import FrontendTestCase

class TestMacanudo(FrontendTestCase):
  def test_crear_macanudo_y_guardarla_en_bd(self):
    macanudo = Macanudo(email='clodo@gmail.com', jornada=100, ocupacion='Desarrollador Web', sueldo=12000, lugar='Chacarita')
    # macanudo = factories.MacanudoFactory(email='clodo@gmail.c')

    db.session.add(macanudo)
    db.session.commit()

    macanudo_en_db = Macanudo.query.all()

    self.assertEquals(len(macanudo_en_db), 1)
    
    unica_macanudo_en_db = macanudo_en_db[0]
    
    self.assertEquals(unica_macanudo_en_db, macanudo)
    self.assertEquals(unica_macanudo_en_db.email, 'clodo@gmail.com')
    self.assertEquals(unica_macanudo_en_db.jornada, Macanudo.FULL_TIME)
    self.assertEquals(unica_macanudo_en_db.ocupacion, 'Desarrollador Web')
    self.assertEquals(unica_macanudo_en_db.sueldo, 12000)
    self.assertEquals(unica_macanudo_en_db.lugar, 'Chacarita')
