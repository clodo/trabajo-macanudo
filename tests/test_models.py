from frontend.models import Postulacion, Tag
from frontend.extensions import db
from tests import FrontendTestCase

class TestPostulacion(FrontendTestCase):
  def test_crear_postulacion_y_guardarla_en_bd(self):
    postulacion = Postulacion()

    postulacion.email = 'clodo@gmail.com'
    postulacion.tipo_pretendido = 100
    postulacion.ocupacion_pretendida = 'Desarrollador Web'
    postulacion.sueldo_pretendido = 12000
    postulacion.lugar_pretendido = 'Chacarita'

    db.session.add(postulacion)
    db.session.commit()

    postulaciones_en_db = Postulacion.query.all()

    self.assertEquals(len(postulaciones_en_db), 1)
    
    unica_postulacion_en_db = postulaciones_en_db[0]
    
    self.assertEquals(unica_postulacion_en_db, postulacion)
    self.assertEquals(unica_postulacion_en_db.email, 'clodo@gmail.com')
    self.assertEquals(unica_postulacion_en_db.tipo_pretendido, 100)
    self.assertEquals(unica_postulacion_en_db.ocupacion_pretendida, 'Desarrollador Web')
    self.assertEquals(unica_postulacion_en_db.sueldo_pretendido, 12000)
    self.assertEquals(unica_postulacion_en_db.lugar_pretendido, 'Chacarita')