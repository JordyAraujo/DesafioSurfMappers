from flask import render_template
from galeriaSM import app

@app.route('/')
@app.route('/index')
def index():
    users = {'Maria', 'Miguel', 'João', 'Amanda'}
    return render_template('index.html', title='Galeria', users=users)