

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from info import profile,deg,core,extended_web,extended_design,extended_content
# import sqlite3
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    def __repr__(self):
        return f"{self.id} - {self.task}"
    # def lst(self):
    #     return list(self.id)
# with app.app_context():
#     db.create_all()


'''
@app.route('/', methods=['GET','POST'])
def hello_world():
    user = User.query.all()
    print(user)
    return render_template('index.html', user=user)
'''
@app.route('/admin/<int:id>')
def delete(id):
    task = User.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/admin')
@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        task_content = request.form['task']
        task_link = request.form['link']
        task1 = User.query.get_or_404(sno)
        task1.link = task_link
        task1.task = task_content
        db.session.add(task1)
        db.session.commit()
        return redirect('/admin')
    tas = User.query.get_or_404(sno)
    return render_template("./admin/update.html", tas = tas)
@app.route('/admin', methods=['GET','POST'])
def about():
    if request.method == 'POST':
        # id = request.form['id']
        task_content = request.form['task']
        task_link = request.form['link']
        new_task = User( task=task_content ,link =task_link)
        db.session.add(new_task)
        db.session.commit()
        # data = User.query.all()
        # print(data)
        return redirect('/admin')
    else:
        
        user = User.query.all()
        # print(User.lst(user))
        return render_template('./admin/admin.html', user=user)

# rough test 
@app.route('/', methods=['GET','POST'])
def hello_world():
    user = User.query.all()
    print(user)
    return render_template('./main/index.html', user=user ,profile = profile,deg =deg,core=core,web =extended_web,design=extended_design,content=extended_content)


    
    

if __name__ == '__main__':
    app.run(debug=True)