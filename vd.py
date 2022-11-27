from flask import Flask,render_template,request
import sqlite3
import os
import pandas as vd
currentdirectory = os.path.dirname(os.path.abspath(__file__))
from openpyxl import load_workbook
app = Flask(__name__)
@app.route('/')
def index_1():
    return render_template('landing.html')
@app.route('/form')
def index_2():
    return render_template('form.html')
@app.route('/form1', methods=['POST','GET'])
def index_3():
    if request.method=='POST':
        receipt_no = request.form['receipt_no']
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        designation = request.form['designation']
        mandal = request.form['mandal']
        district = request.form['district']
        amount = request.form['amount']
        connection = sqlite3.connect(currentdirectory+"/vd.db")
        cursor = connection.cursor()
        deexu = "INSERT INTO vd VALUES('{receipt_no}','{employee_id}','{employee_name}','{designation}','{mandal}','{district}','{amount}')".format(receipt_no=receipt_no,employee_id=employee_id,employee_name=employee_name,designation=designation,mandal=mandal,district=district,amount=amount)
        cursor.execute(deexu)
        connection.commit()
        sd = vd.read_sql_query("SELECT * from vd",connection)
        sd.to_excel("{}.xlsx".format("data"))
        return render_template('index.html',rno=receipt_no,eid=employee_id,ename=employee_name,desig=designation,man=mandal,dist=district,amt=amount)
    return render_template('index.html')
@app.route('/history')
def index_4():
    wb = load_workbook("data.xlsx")
    sheet = wb.active
    return render_template('history.html',sheet=sheet)
app.run()