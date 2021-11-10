from flask import render_template, request, redirect, url_for, Flask, session, abort, flash
from flask_wtf import Form
import os, gc
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf  import CSRFProtect
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy import Column,  String
from importlib import reload
import sqlalchemy as sa
import sys
reload(sys)

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from config import app
from database import db_session
import services

sa.create_engine('postgresql://postgres:thanhnho@localhost:5432/phunhuan')

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:thanhnho@localhost:5432/phunhuan'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

app = Flask(__name__, static_folder='C:\\xampp\\tomcat\\webapps\\Flaskapp' )
app = Flask(__name__, static_folder='C:\\xampp\\tomcat\\webapps\\Flaskapp\\templates\\static' )

@app.route('/', methods = ['GET', 'POST'])
def map():
    diachi= request.args.get('diachi', "" )
    phuong= request.args.get('phuong', "" )
    dienthoai= request.args.get('dienthoai', "" )
    lienhe= request.args.get('lienhe', "" )
    dientich = request.args.get('dientich', "")
    gia = request.args.get('gia',  "") 
    dien= request.args.get('dien',  "" )
    nuoc= request.args.get('nuoc',  "" )
    dichvu= request.args.get('dichvu',  "" )
    giogiac= request.args.get('giogiac', "" )
    noithat= request.args.get('noithat', "" )
    songuoi = request.args.get('songuoi',  "")
    ghichu= request.args.get('ghichu',  "" )
    result = []
    sql_str = "-----"
    list_phongtro = [] 	

    if dientich and gia  and  phuong and diachi or lienhe or dienthoai or dien or nuoc or dichvu or giogiac or noithat or songuoi or ghichu  :
 
        dientich = str(dientich)
        gia = str(gia)
        phuong = str(phuong)
        diachi = str(diachi)
        lienhe = str(lienhe)
        dienthoai = str(dienthoai)
        dien = str(dien)
        nuoc = str(nuoc)
        dichvu = str(dichvu)
        noithat = str(noithat)
        giogiac = str(giogiac)
        songuoi = str(songuoi)
        ghichu = str(ghichu)
        
        sql_str, list_phongtro = services.getData(phuong, dientich, gia, diachi, lienhe, dienthoai, dien, nuoc, dichvu, songuoi, noithat, giogiac, ghichu)
        result = [] #services.chkCondition(dientich, gia, songuoi, loaihinhtr, gioitinh, giogiac, diachi, lienhe, dienthoai, dien, nuoc, dichvu, tien_guixe, osm_id,name, doituong)
            #result = services.convertChkResultToData(result)                        
    return render_template('index.html', sql_str = sql_str, result=result, list_phongtro=list_phongtro)

class phongtro_phunhuan(db.Model):
    __tablename__ = 'phongtro_phunhuan'  
    #gid = Column(String(10), primary_key=True)
    dientich  = Column(String(10), primary_key=True)
    gia  = Column(String(10) )
    dien = Column(String(10))
    nuoc = Column(String(10))
    dichvu = Column(String(10))
    songuoi = Column( String(10))
    noithat  = Column(String (50))
    giogiac  = Column(String (50))
    ghichu  = Column(String (50))
    diachi  = Column(String (250))
    phuong = Column(String(10))  
    lienhe  = Column(String (50)) 
    dienthoai  = Column(String (50))
    
    def __init__(self  , diachi, phuong, lienhe, dienthoai, dientich , gia, dien, nuoc, dichvu, songuoi, giogiac, noithat, ghichu):
        self.diachi = diachi
        self.phuong = phuong
        self.lienhe = lienhe
        self.dienthoai = dienthoai
        self.dientich = dientich
        self.gia = gia
        self.dien = dien
        self.nuoc = nuoc
        self.dichvu = dichvu
        self.songuoi = songuoi
        self.giogiac = giogiac 
        self.noithat = noithat
        self.ghichu = ghichu

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        phongtro = phongtro_phunhuan(phuong=request.form['phuong'] ,dientich=request.form['dientich'], gia=request.form['gia'],songuoi=request.form['songuoi'], giogiac=request.form['giogiac'], diachi=request.form['diachi'],dien=request.form['dien'], nuoc=request.form['nuoc'], dichvu=request.form['dichvu'], ghichu=request.form['ghichu'], lienhe=request.form['lienhe'], dienthoai=request.form['dienthoai'] )
        db.session.add(phongtro)
        db.session.commit()
        return render_template('post.html')
    return render_template('post.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/introduce')
def introduce():
    return render_template('introduce.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
    
