import pyodbc 
import xlrd
import os
from datetime import datetime
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '10.13.26.40' 
database = 'db_visual_rodopar' 
username = 'cyber' 
password = 'bycyber' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
#cursor.execute("SELECT * from ime_rv_usuarios;") 
#row = cursor.fetchone() 
#while row: 
    #print(row[0])
    #row = cursor.fetchone()

book = xlrd.open_workbook("C:/Users/CTOSMGBit/Documents/IMPORTACAO DISPONIBILIDADE.xlsx")
sheet = book.sheet_by_name("JUL-2019")
datas = []
for r in range(2, sheet.ncols):
    datas.append(sheet.cell(0, r).value)
for p in range(1, sheet.nrows):
    for c in range(2, sheet.ncols):
        placa = sheet.cell(p,0).value
        data = datas[c-2]
        status = sheet.cell(p,1).value
        sigla = sheet.cell(p,c).value
        print(placa + '-' + data + '-' + status + '-' + sigla)
        cursor.execute("INSERT INTO SMG_FROTAS_DISPONIBILIDADE (PLACA,DATDIS, STATUS,MOTIVO,SIGLA) VALUES ('" + placa.replace('-','') + "','" + data + "','" + status + "','" + sigla + "','" + sigla + "')") 
        cnxn.commit()