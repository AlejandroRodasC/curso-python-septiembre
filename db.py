#SELECT nombre, fecha_nacimiento, carnet FROM alumnos;
#CRUD -- Create Read Update Delete

from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy import Column, String, Integer, create_engine, update, delete, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
engine = create_engine("sqlite:///:memory:")

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombre =  Column(String, nullable=False)
    apellidos = Column(String)
    carnet =  Column(Integer)
    notas = relationship('Nota', back_populates='alumno')

    @hybrid_property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"
        
    def __repr__(self) -> str:
        return self.nombre_completo

class Nota (Base):
    __tablename__ = 'notas'
    id = Column(Integer,primary_key=True)
    curso = Column(String)
    alumno_id = Column(Integer, ForeignKey('alumnos.id'))
    alumno = relationship('Alumno', back_populates='notas')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

alumno = Alumno(
    nombre = 'Alejandro',
    apellidos = 'Rodas',
    carnet = 202040001
)


session.add(alumno)
session.commit()

alumno = Alumno(
    nombre = 'Edwin',
    apellidos = 'Carranza',
    carnet = 202040001
)


session.add(alumno)
session.commit()
session.refresh(alumno)

alumno_db = session.query(Alumno).where(Alumno.nombre == 'Alejandro').first()



alumnos = session.query(Alumno).all()
print(alumnos)
print(alumnos[0].nombre_completo)
print(alumnos[1].nombre_completo)

cantidad_alumnos = session.query(Alumno).count()
print(cantidad_alumnos)

edwin = session.query(Alumno).where(Alumno.id==2).first()
edwin.apellidos = 'Carranza 2'
session.add(edwin)
session.commit()


edwin_db = session.query(Alumno).where(Alumno.id==2).first()
print(edwin_db.apellidos)

actualizacion = update(Alumno).values(carnet=99999)
session.execute(actualizacion)

alumno1 = session.query(Alumno).first()
print(alumno1.carnet)

borrado = delete(Alumno).where(Alumno.id == 1)
session.execute(borrado)

alumno1 = session.query(Alumno).where(Alumno.id == 1).first()



nota = Nota(
    curso = 'Matematicas',
    alumno_id = 2    
)
session.add(nota) 
session.commit()
print(nota.alumno_id)
print(nota.alumno.carnet)
print(nota.alumno.notas[0].curso)   