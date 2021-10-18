from pathlib import Path
import os
import socket
import time
from flask import Flask, request, jsonify, render_template, send_from_directory
import qrcode
from PIL import Image
#import mysql.connector
import pyodbc

#get IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
except Exception:
    IP = '127.0.0.1'
finally:
    s.close()
   

PORT = 8050 #change this to desired port
# lsof -ti:8000 | xargs kill 
localFolderDownloads = 'Downloads/QRCODES-DB' #change this to desired directory
pk = 'col_2' #change this to desired directory

# web_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', localFolder))

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="dims-II"
# )



#cursor = mydb.cursor()
#cursor.execute("select a.cos_sec, a.part_no, a.nomen1, b.stok_free, b.mmf, b.msp from dbo.mpi_file a inner join dbo.stokfile b on a.part_no=  b.part_no ")
mydb = pyodbc.connect("DRIVER={SQL Server};"
                      "Server=localhost\SQLEXPRESS;"
                      "Database=dims-II;"
                      "Trusted_Connection=yes;")

def query(pk= False, pkvalue=False):
    results = []
    with mydb:
        cur = mydb.cursor()
        if(pkvalue and pk):
            query = "select a.cos_sec, a.part_no, a.nomen1, b.stok_free, b.mmf, b.msp from dbo.mpi_file a inner join dbo.stokfile b on a.part_no=  b.part_no where a.part_no  = '"+pkvalue+"'"
        elif(pk):
            query = "SELECT TOP 100 a.part_no from dbo.mpi_file a inner join dbo.stokfile b on a.part_no=  b.part_no "
        else:
            query = "select a.cos_sec, a.part_no, a.nomen1, b.stok_free, b.mmf, b.msp from dbo.mpi_file a inner join dbo.stokfile b on a.part_no=  b.part_no"
        print(query)
        cur.execute(query)
    #articles = cur.fetchall()

        columns = [column[0] for column in cur.description]
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
    #mydb.close()
    return results

def keyArray():
    arr = [];
    #for x in query(pk):
     #   arr.append(x[pk])
    return arr



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html', arr=keyArray())


@app.route('/custom/js/<path:filename>')
def custom_static_js(filename):
    return send_from_directory(app.root_path + '/custom/js/', filename)


@app.route('/custom/css/<path:filename>')
def custom_static_css(filename):
    return send_from_directory(app.root_path + '/custom/css/', filename)



@app.route('/gen', methods=[ 'POST']) 
def gen():
    print(request) 
    link = request.json["link"]
    fname = request.json["fname"]
    imgQr = qrcode.make(link)
    downloads_path = str(Path.home() / localFolderDownloads)

    isFile = os.path.exists(downloads_path.strip()) #stip the path and check if it exists
    # make directory if not exists
    if(not isFile):
        os.mkdir(downloads_path)
    
    imgQr.save(downloads_path+'/'+fname+"_QR.jpg")
    print('saving')
    return {"success" :"true"}


@app.route('/details', methods=[ 'GET']) 
def details():
    print(request) 
    id = request.args.get("id")
    result = query(pk , id)
    #result = []
    return render_template('index.html', result=result)

if(int(time.time())<1635033599):
    if(IP):
        if __name__=="__main__":
            app.run(host=IP, port=PORT, debug=True)
    else:   
        if __name__=="__main__":
            app.run(host="localhost", port=PORT) 
