import factories
from frontend.models import Empleo, Tag
from frontend.extensions import db
from tests import FrontendTestCase

class TestEmpleo(FrontendTestCase):
  def test_crear_empleo_y_guardarla_en_bd(self):
    empleo = Empleo(email='clodo@gmail.com', jornada=100, ocupacion='Desarrollador Web', sueldo=12000, lugar='Chacarita')
    # empleo = factories.EmpleoFactory(email='clodo@gmail.c')

    db.session.add(empleo)
    db.session.commit()

    empleo_en_db = Empleo.query.all()

    self.assertEquals(len(empleo_en_db), 1)
    
    unica_empleo_en_db = empleo_en_db[0]
    
    self.assertEquals(unica_empleo_en_db, empleo)
    self.assertEquals(unica_empleo_en_db.email, 'clodo@gmail.com')
    self.assertEquals(unica_empleo_en_db.jornada, Empleo.FULL_TIME)
    self.assertEquals(unica_empleo_en_db.ocupacion, 'Desarrollador Web')
    self.assertEquals(unica_empleo_en_db.sueldo, 12000)
    self.assertEquals(unica_empleo_en_db.lugar, 'Chacarita')