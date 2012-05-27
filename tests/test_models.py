from frontend.models import Postulacion, Tag
from frontend.extensions import db
from tests import FrontendTestCase

class TestPostulacion(FrontendTestCase):
  def test_crear_postulacion_y_guardarla_en_bd(self):
    postulacion = Postulacion(email='clodo@gmail.com', jornada=100, ocupacion='Desarrollador Web', sueldo=12000, lugar='Chacarita')

    db.session.add(postulacion)
    db.session.commit()

    postulaciones_en_db = Postulacion.query.all()

    self.assertEquals(len(postulaciones_en_db), 1)
    
    unica_postulacion_en_db = postulaciones_en_db[0]
    
    self.assertEquals(unica_postulacion_en_db, postulacion)
    self.assertEquals(unica_postulacion_en_db.email, 'clodo@gmail.com')
    self.assertEquals(unica_postulacion_en_db.jornada, Postulacion.FULL_TIME)
    self.assertEquals(unica_postulacion_en_db.ocupacion, 'Desarrollador Web')
    self.assertEquals(unica_postulacion_en_db.sueldo, 12000)
    self.assertEquals(unica_postulacion_en_db.lugar, 'Chacarita')

#  def test_postulacion_sabe_guardar_tags(self):
#    tag_php = Tag(name='php')

#    db.session.add(tag_php)
#    db.session.commit()

#    postulacion = Postulacion(email='clodo@gmail.com', jornada=100, ocupacion='Desarrollador Web', sueldo=12000, lugar='Chacarita')

#    postulacion.tags = "php, python, php, mysql"

#    db.session.add(postulacion)
#    db.session.commit()

#    self.assertEquals(len(postulacion.tags), 3)
#    self.assertEquals(len(Tag.query.all()), 3)