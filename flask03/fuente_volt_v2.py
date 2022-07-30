from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float

#pip install Flask-Bootstrap
#pip install Flask-WTF
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)


#pip install Flask-WTF
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField


class FormCalculadora(FlaskForm):
    vol = IntegerField("Número0")
    num1 = IntegerField("Número1")
    num2 = IntegerField("Número2")
    submit = SubmitField('Submit')

@app.route('/')
def inicio():
    session2 = Session()
    r= '''
<!doctype html>
<html>
<head>
	<title>Fuentes de voltaje!</title>
</head>
<body>
	<h1>Listado</h1>
    '''+(
	''.join(['<p>'+str((f_v.voltios, f_v.nodo_mas, f_v.nodo_menos))+'</p>' for f_v in session2.query(FuenteVoltaje).all()])  
    )+'''
	<a href="/adicionar" >Adicionar</a>
</body>
</html>   '''
    session2.close()
    return r


@app.route("/adicionar", methods=["get", "post"])
def calculadora_post():
    form = FormCalculadora(request.form)
    if form.validate_on_submit():
        vol = form.vol.data
        num1 = form.num1.data
        num2 = form.num2.data
        session.add(FuenteVoltaje(vol, num1, num2))
        session.commit()
    return render_template("adicionar.html", form=form)
 
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

if __name__ == "__main__":  
    Base.metadata.create_all(engine)
    app.run(
		host='localhost',  
		port=5003  
	)

