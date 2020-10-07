from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = {'Joao', 'Miguel', 'Maria', 'Amanda'}
    return render_template('index.html', title='Galeria', users=users)