import pyodbc
from pathlib import Path
import os
import socket
from flask import Flask, request, jsonify, render_template, send_from_directory
import qrcode
from PIL import Image
from PIL import Image
app = Flask(__name__)
localFolderDownloads = 'Downloads/QRCODES' #change this to desired directory

#sqlcode
cnxn = pyodbc.connect("DRIVER={SQL Server};"
                      "Server=localhost\SQLEXPRESS;"
                      "Database=dims-II;"
                      "Trusted_Connection=True;")

cursor = cnxn.cursor()
cursor.execute("select a.cos_sec, a.part_no, a.nomen1, b.stok_free, b.mmf, b.msp from dbo.mpi_file a inner join dbo.stokfile b on a.part_no=  b.part_no ")

#for row in cursor:

   # print('row = %r' % (row,))

#QRcode
#@app.route('/gen', methods=['POST'])
def gen():
    print(request)
    link = request.json["N2,HK-670127 E,DESCRIPTION HAND BOOK,0.000,0.000,3.000"]
    #fname = request.json["fname"]
    imgQr = qrcode.make("N2,HK-670127E,DESCRIPTION HAND BOOK,0.000,0.000,3.000")
    downloads_path = str(Path.home() / localFolderDownloads)

    isFile = os.path.exists(downloads_path.strip())  # stip the path and check if it exists
    # make directory if not exists
    if (not isFile):
        os.mkdir(downloads_path)

    imgQr.save(downloads_path + '/' + fname + "_QR.jpg")
    print('saving')
    return {"success": "true"}



#connection string = Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;
#C:\Program Files\Microsoft SQL Server\150\Setup Bootstrap\Log\20210927_135703
#media folder = C:\SQL2019\Express_ENU
#resources folder =  C:\Program Files\Microsoft SQL Server\150\SSEI\Resources
#dbo.MSreplication_options