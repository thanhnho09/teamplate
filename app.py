
from flask import Flask, render_template, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2  # pip install psycopg2
import psycopg2.extras
from geoalchemy2 import Geometry


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:thanhnho@localhost/phunhuan'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)

app.secret_key = "tn"

DB_HOST = "localhost"
DB_NAME = "phunhuan"
DB_USER = "postgres"
DB_PASS = "thanhnho"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


class phongtro(db.Model):
    gid = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)
    diachi = db.Column(db.String(200), nullable=False)
    phuong = db.Column(db.String)
    dientich = db.Column(db.String)
    gia = db.Column(db.String)
    dien = db.Column(db.String)
    nuoc = db.Column(db.String)
    dichvu = db.Column(db.String)
    noithat = db.Column(db.String)
    songuoi = db.Column(db.Integer)
    ghichu = db.Column(db.String)
    lienhe = db.Column(db.String)
    dienthoai = db.Column(db.String)
    geom = db.Column(Geometry('POINT'))

    def __init__(self, longitude, latitude, diachi, phuong, dientich, gia, dien, nuoc, dichvu, noithat, songuoi, ghichu, lienhe, dienthoai):
        self.longitude = longitude
        self.latitude = latitude
        self.diachi = diachi
        self.phuong = phuong
        self.dientich = dientich
        self.gia = gia
        self.dien = dien
        self.nuoc = nuoc
        self.dichvu = dichvu
        self.noithat = noithat
        self.songuoi = songuoi
        self.ghichu = ghichu
        self.lienhe = lienhe
        self.dienthoai = dienthoai


@app.route('/sort')
def sort():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y,  * FROM phongtro")
        gia = cursor.fetchall()
        return render_template('sort.html', gia=gia)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/fetchdeta", methods=["POST", "GET"])
def fetchdeta():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            min = request.form['min']
            max = request.form['max']
            cursor.execute(
                "SELECT ST_X(geom) as x, ST_Y(geom) as y,  * FROM phongtro  WHERE gia>=(%s) AND gia<=(%s)", [min, max, ])
            gia = cursor.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', gia=gia)})
    except Exception as e:
        print(e)


@app.route('/sort_s')
def sort_s():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y,  * FROM phongtro")
        dientich = cursor.fetchall()
        return render_template('sort_s.html', dientich=dientich)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/fetchdetaa", methods=["POST", "GET"])
def fetchdetaa():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            min = request.form['min']
            max = request.form['max']
            cursor.execute(
                "SELECT ST_X(geom) as x, ST_Y(geom) as y,  * FROM phongtro  WHERE dientich>=(%s) AND dientich<=(%s)", [min, max, ])
            dientich = cursor.fetchall()
            return jsonify({'htmls': render_template('s.html', dientich=dientich)})
    except Exception as e:
        print(e)


@app.route("/phuong1", methods=["POST", "GET"])
def phuong1():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong1 = "'Phường 1'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong1))
        phuong1 = cursor.fetchall()
        return render_template('sort_1.html', phuong1=phuong1)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong2", methods=["POST", "GET"])
def phuong2():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong2 = "'Phường 2'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong2))
        phuong2 = cursor.fetchall()
        return render_template('sort_2.html', phuong2=phuong2)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong3", methods=["POST", "GET"])
def phuong3():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong3 = "'Phường 3'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong3))
        phuong3 = cursor.fetchall()
        return render_template('sort_3.html', phuong3=phuong3)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong4", methods=["POST", "GET"])
def phuong4():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong4 = "'Phường 4'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong4))
        phuong4 = cursor.fetchall()
        return render_template('sort_4.html', phuong4=phuong4)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong5", methods=["POST", "GET"])
def phuong5():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong5 = "'Phường 5'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong5))
        phuong5 = cursor.fetchall()
        return render_template('sort_5.html', phuong5=phuong5)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong", methods=["POST", "GET"])
def phuong():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuongb = "'Phường 7'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuongb))
        phuong = cursor.fetchall()
        return render_template('sort_p.html', phuong=phuong)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong8", methods=["POST", "GET"])
def phuong8():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong8 = "'Phường 8'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong8))
        phuong8 = cursor.fetchall()
        return render_template('sort_8.html', phuong8=phuong8)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong9", methods=["POST", "GET"])
def phuong9():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong9 = "'Phường 9'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong9))
        phuong9 = cursor.fetchall()
        return render_template('sort_9.html', phuong9=phuong9)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong10", methods=["POST", "GET"])
def phuong10():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong10 = "'Phường 10'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong10))
        phuong10 = cursor.fetchall()
        return render_template('sort_10.html', phuong10=phuong10)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong11", methods=["POST", "GET"])
def phuong11():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong11 = "'Phường 11'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y,* from phongtro WHERE phuong = {}".format(phuong11))
        phuong11 = cursor.fetchall()
        return render_template('sort_11.html', phuong11=phuong11)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong12", methods=["POST", "GET"])
def phuong12():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong12 = "'Phường 12'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong12))
        phuong12 = cursor.fetchall()
        return render_template('sort_12.html', phuong12=phuong12)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong13", methods=["POST", "GET"])
def phuong13():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong13 = "'Phường 13'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong13))
        phuong13 = cursor.fetchall()
        return render_template('sort_13.html', phuong13=phuong13)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong14", methods=["POST", "GET"])
def phuong14():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong14 = "'Phường 14'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong14))
        phuong14 = cursor.fetchall()
        return render_template('sort_14.html', phuong14=phuong14)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong15", methods=["POST", "GET"])
def phuong15():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong15 = "'Phường 15'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong15))
        phuong15 = cursor.fetchall()
        return render_template('sort_15.html', phuong15=phuong15)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/phuong17", methods=["POST", "GET"])
def phuong17():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        phuong17 = "'Phường 17'"
        cursor.execute(
            "SELECT ST_X(geom) as x, ST_Y(geom) as y, * from phongtro WHERE phuong = {}".format(phuong17))
        phuong17 = cursor.fetchall()
        return render_template('sort_17.html', phuong17=phuong17)
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.route("/add")
def add():
    return render_template("post.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        lienhe = request.form["lienhe"]
        dienthoai = request.form["dienthoai"]
        diachi = request.form["diachi"]
        phuong = request.form["phuong"]
        gia = request.form["gia"]
        dientich = request.form["dientich"]
        dien = request.form["dien"]
        nuoc = request.form["nuoc"]
        dichvu = request.form["dichvu"]
        noithat = request.form["noithat"]
        songuoi = request.form["songuoi"]
        giogiac = request.form["giogiac"]
        ghichu = request.form["ghichu"]
        lat = request.form["lat"]
        lon = request.form["lon"]
        cur.execute(
            "INSERT INTO phongtro ( lienhe, dienthoai, diachi, phuong, gia, dientich, dien, nuoc, dichvu, noithat, songuoi, giogiac, ghichu, geom) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', ST_GeomFromText('point ({}  {})'))".format(lienhe, dienthoai, diachi, phuong, gia, dientich, dien, nuoc, dichvu, noithat, songuoi, giogiac, ghichu, lat, lon))
        conn.commit()
        return render_template("post.html")


@app.route('/show')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM phongtro"
    cur.execute(s)  # Execute the SQL
    show_phongtro = cur.fetchall()
    return render_template('show.html', show_phongtro=show_phongtro)


@app.route('/delete/<string:gid>', methods=['POST', 'GET'])
def delete_student(gid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DELETE FROM phongtro WHERE gid = {0}'.format(gid))
    conn.commit()
    flash('Removed Successfully')
    return render_template('show.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/introduce')
def introduce():
    return render_template('introduce.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/list_phuong')
def list_phuong():
    return render_template('list_phuong.html')


if __name__ == '__main__':
    app.run(host='localhost', port=9847)
