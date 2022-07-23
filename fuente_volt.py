from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('sqlite:///productos.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class FuenteVoltaje(Base):
    __tablename__ = 'FuenteVoltaje'
    id = Column(Integer, primary_key=True)
    voltios = Column(Float)
    nodo_mas = Column(Integer)
    nodo_menos = Column(Integer)

    def __init__(self, voltios, nodo_mas, nodo_menos):
        self.voltios = voltios
        self.nodo_mas = nodo_mas
        self.nodo_menos = nodo_menos


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    while True:
        print('Seleccione una opción')
        print('1 Adicionar una fuente de voltaje')
        print('2 Mostrar las fuentes de voltaje')
        print('3 Borrar una fuente de voltaje')
        print('4 Modificar una fuente de voltaje')
        print('5 Salir')
        opcion = input().strip()

        if opcion == '1':
            voltaje = input('Escriba el voltaje: ')
            nodo1 = input('Escriba el nodo 1: ')
            nodo2 = input('Escriba el nodo 2: ')
            session.add(FuenteVoltaje(voltaje, nodo1, nodo2))
            session.commit()

        elif opcion == '2':
            for f_v in session.query(FuenteVoltaje).all():
                print(f_v.voltios, f_v.nodo_mas, f_v.nodo_menos)

        elif opcion == '3':
            i = int(input('Escriba el índice: '))
            f_v = session.query(FuenteVoltaje).get(i)
            session.delete(f_v)
            session.commit()

        elif opcion == '4':
            i = int(input('Escriba el índice: '))
            f_v = session.query(FuenteVoltaje).get(i)
            print(i, f_v.voltios, f_v.nodo_mas, f_v.nodo_menos)
            voltaje = input('Escriba el voltaje: ')
            if voltaje != '':
                f_v.voltios = voltaje
            nodo1 = input('Escriba el nodo 1: ')
            if nodo1 != '':
                f_v.nodo_mas = nodo1
            nodo2 = input('Escriba el nodo 2: ')
            if nodo2 != '':
                f_v.nodo_menos = nodo2
            session.commit()

        elif opcion == '5':
            break

        else:
            print(f'"{opcion}" no es una opción válida')

session.close()
engine.dispose()
