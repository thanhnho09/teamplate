import sys
from importlib import reload
reload(sys)
const_timestr = '000000000000000000000'
const_sodiem = 2**21

def getData( diachi="", phuong="", dientich ="", gia="",   
            lienhe = "", dienthoai = "", dien ="", nuoc ="", dichvu="", giogiac="", noithat="", songuoi="", ghichu=""  ):
  cau_where = "where phongtro_phunhuan"
  if (dientich != ""):
      if (dientich == '1'):
        cau_where = cau_where + " and phongtro_phunhuan.dientich >= 10 and phongtro_phunhuan.dientich < 15 " 
      if (dientich == '2'):
        cau_where = cau_where + " and phongtro_phunhuan.dientich >= 15 and phongtro_phunhuan.dientich < 20 "
      if (dientich == '3'):
        cau_where = cau_where + " and phongtro_phunhuan.dientich >= 20 and phongtro_phunhuan.dientich < 25 " 
      if (dientich == '4'):
        cau_where = cau_where + " and phongtro_phunhuan.dientich > 25 " 
  if (gia != ""):
      if (gia == '1'):
        cau_where = cau_where + " and phongtro_phunhuan.gia >=2 and phongtro_phunhuan.gia <3"
      if (gia == '2'):
        cau_where = cau_where + " and phongtro_phunhuan.gia >=3 and phongtro_phunhuan.gia <4"
      if (gia == '3'):
        cau_where = cau_where + " and phongtro_phunhuan.gia >=4 and phongtro_phunhuan.gia <5"      

  if (phuong != ""):
      if (phuong == '1'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 1%'" 
      if (phuong == '2'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 2%'" 
      if (phuong == '3'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 3%'" 
      if (phuong == '4'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 4%'" 
      if (phuong == '5'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 5%'" 
      if (phuong == '7'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 7%'" 
      if (phuong == '8'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 8%'" 
      if (phuong == '9'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 9%'" 
      if (phuong == '10'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 10%'" 
      if (phuong == '11'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 11%'" 
      if (phuong == '12'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 12%'" 
      if (phuong == '13'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 13%'" 
      if (phuong == '14'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 14%'" 
      if (phuong == '15'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 15%'" 
      if (phuong == '17'):
        cau_where = cau_where + " and phongtro_phunhuan.phuong like '%Phường 17%'" 
  
  
  if (diachi != ""):
        cau_where = cau_where + " and phongtro_phunhuan.diachi = " + str(diachi)
  if (lienhe != ""):
        cau_where = cau_where + " and phongtro_phunhuan.lienhe = '" + lienhe + "'"
  if (dienthoai != ""):
        cau_where = cau_where + " and phongtro_phunhuan.dienthoai = '" + str(dienthoai) + "'"
  if (dien != ""):
        cau_where = cau_where + " and phongtro_phunhuan.dien = " + str(dien)
  if (nuoc != ""):
        cau_where = cau_where + " and phongtro_phunhuan.nuoc = " + str(nuoc)
  if (dichvu != ""):
        cau_where = cau_where + " and phongtro_phunhuan.dichvu = " + str(dichvu)
  if (giogiac != ""):
        cau_where = cau_where + " and phongtro_phunhuan.giogiac = " + str(giogiac)
  if (noithat != ""):
        cau_where = cau_where + " and phongtro_phunhuan.noithat = " + str(noithat)
  if (songuoi != ""):
        cau_where = cau_where + " and phongtro_phunhuan.songuoi = " + str(songuoi)
  if (ghichu != ""):
        cau_where = cau_where + " and phongtro_phunhuan.ghichu = " + str(ghichu)

  
  #return cau_where
  from database import db_session  		
#  data = db_session().execute('select * from phongtro_phunhuan where phongtro_phunhuan')
  sql_str = 'select * from phongtro_phunhuan ' + cau_where
  data = db_session().execute(sql_str)
  list = []
  for row in data:
        phongtro = convertRowDataTophongtro(row)
        list.append(phongtro)
  return sql_str, list
	
def convertRowDataTophongtro(row):
    return {'gid': row['gid'], 'y':row['longitude'],'x': row['latitude'], 'diachi': row['diachi'],'phuong': row['phuong'],'dientich': row['dientich'],'gia': row['gia'],'lienhe': row['lienhe'],'dienthoai':row['dienthoai'],'dien':row['dien'],'nuoc':row['nuoc'],'dichvu':row['dichvu'], 'giogiac':row['giogiac'], 'noithat': row['noithat'], 'songuoi':row['songuoi'], 'ghichu': row['ghichu'],}
	
