from flask import Flask, render_template, request, redirect
from datetime import date
from flask_sqlalchemy import SQLAlchemy
today = date.today()
stringDay = f'{today.day} / {today.month} / {today.year}'


# STUDENT AP #
app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentAP.db'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
d1b = SQLAlchemy(app1)

class StudentsAP(d1b.Model):
    snnm = d1b.Column(d1b.Integer,primary_key=True)
    name1m = d1b.Column(d1b.String(100))
    ronm = d1b.Column(d1b.Integer)
    apm = d1b.Column(d1b.String(55), nullable=False , default='A')
    apDatem = d1b.Column(d1b.String(55),default=stringDay)
    def __repr__(self):
        return f'{self.snnm} - {self.name1m} - {self.ronm} - {self.apm} - {self.apDatem}'

def call():
    return StudentsAP.query.all()

def dele(r):
    stDelete = StudentsAP.query.filter_by(ronm=r).first()
    d1b.session.delete(stDelete)
    d1b.session.commit()
# STUDENT AP #















app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Students(db.Model):
    snn = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(100))
    ron = db.Column(db.Integer)
    bid = db.Column(db.String(55))
    admi = db.Column(db.String(55),default=stringDay)
    res = db.Column(db.String(55))
    def __repr__(self):
        return f'{self.snn} - {self.name1} - {self.ron} - {self.bid} - {self.admi} - {self.res}'
@app.route('/', methods=['POST','GET'])
def hello():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
    if request.method == 'POST':
        name1 = request.form['name1']
        ron = request.form['ron']
        bid = request.form['bid']
        if request.form['admi'] == '':
            admi = stringDay
        else:
            admi = request.form['admi']
        res = request.form['res']
        Panther = Students(name1=name1,ron=ron,bid=bid,res=res,admi=admi)
        db.session.add(Panther)
        db.session.commit()
    allStudents = Students.query.all()
    return render_template('index.html',dddb=app.config['SQLALCHEMY_DATABASE_URI'], allStudents=allStudents)

@app.route('/panther')
def panther_pr():
    return render_template('p.html')

@app.route('/update/<int:snn>', methods=['GET', 'POST'])
def upd(snn):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
    SNoData = Students.query.filter_by(snn=snn).first() 
    if request.method == 'POST':
        name1 = request.form['name1']
        ron = request.form['ron']
        bid = request.form['bid']
        if request.form['admi'] == '':
            admi = stringDay
        else:
            admi = request.form['admi']
        res = request.form['res']
        SNoData.name1 = name1
        SNoData.ron = ron
        SNoData.bid = bid
        SNoData.admi = admi
        SNoData.res = res
        db.session.add(SNoData)
        db.session.commit()
        return redirect('/')
    return render_template('update.html', SNoData=SNoData)

@app.route('/ap', methods=['POST', 'GET'])
def abpr():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
    if request.method == 'POST':
        ron = request.form['ron1']
        if request.form['ap1'] == 'a' or request.form['ap1'] == 'A':
            ap = 'Absent'
        elif request.form['ap1'] == 'p' or request.form['ap1'] == 'P':
            ap = 'Present'
        else:
            ap = 'taken hollyday'
        if request.form['apd1'] == '':
            apd1 = stringDay
        else:
            apd1 = request.form['apd1']
        SNoData = Students.query.filter_by(ron=ron).first()
        name = SNoData.name1
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentAP.db'
        fire = StudentsAP(name1m=name,ronm=ron,apm=ap,apDatem=apd1)
        d1b.session.add(fire)
        d1b.session.commit()
        allAPs = call()
        return render_template('ab-pr.html', Sts=allAPs)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentAP.db'
    allAPs = call()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
    return render_template('ab-pr.html',Sts=allAPs)
@app.route('/delete/<int:snn>', methods=['GET','POST'])
def dell(snn):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentEx.db'
    stDelete = Students.query.filter_by(snn=snn).first()
    db.session.delete(stDelete)
    db.session.commit()
    return redirect('/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentAP.db'
@app.route('/APD/<int:ron>', methods=['GET','POST'])
def deleAP1(ron):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentAP.db'
    dele(ron)
    return redirect('/ap')

# Runner....
if __name__ == "__main__":
    app.run(debug=True ,port=5000)



# || database created success fully ||
# creation database == studentEx.db

'''
-----------------------
database = stud.db
html = index.html
-----------------------


_______________________________
---> variables
SNo, name, ron, bid, admi, res
_______________________________


***************************************
port = 8010
web = http://127.0.0.1:5000
***************************************


-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
add format ---> Panther = Student(name="dhruv",ron=11,bid='7-10-2022',res='News Paper') <---
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


*************************************************************
flask_sqlalchemy  version  2.5.1
problem  solution  video  https://youtu.be/QBpUgbW6qhw
*************************************************************

'''

