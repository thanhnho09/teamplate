from sqlalchemy import Column, Integer, Text, Numeric
from config import db

# đọc các trường trong bảng  phòng trọ
class phongtro(db.Model):
    __tablename__ = 'phongtro_phunhuan'  #ten bang csdl
    gid = db.Column(db.Integer, primary_key=True)
    longitude  = db.Column(db.Numeric)
    latitude  = db.Column(db.Numeric)
    diachi  = db.Column(db.Text)
    phuong  = db.Column(db.Text)
    lienhe  = db.Column(db.Text)
    dienthoai = db.Column(db.Text)
    dientich  = db.Column(db.Text)
    gia  = db.Column(db.Text)
    dien = db.Column(db.Text)
    nuoc = db.Column(db.Text)
    dichvu = db.Column(db.Text)
    giogiac = db.Column(db.Text)
    noithat = db.Column(db.Text)
    songuoi = db.Column(db.Integer)
    ghichu = db.Column(db.Text)
    
    def __init__(self, kyhieu_qh):  # khoi tao
        self.kyhieu_qh = kyhieu_qh
