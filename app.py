from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'
db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    zag = db.Column(db.String(128), nullable=False)
    tex = db.Column(db.Text, nullable=False)
    fl = db.Column(db.String(128), nullable=False)


@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        zag = request.form.get('Tem')
        tex = request.form.get('Mes')
        dt = request.form.get('dt')
        fl =  request.form.get('fl')
        c = News(zag=zag, tex=tex, dt=dt)
        db.session.add(c)
        db.session.commit()
        if fl:
            r = fl.filename.split('.')[-1]
            if r == 'jpg' or r == 'jpeg' or r == 'png':
                filename1 =

        return redirect('/')
    return render_template('write.html')


@app.route('/view')
def view():
    a = News.query.order_by(News.id).all()
    return render_template('view.html', a=a)


app.run(host='127.0.0.1', debug=True)
