from flask import render_template, flash, request, redirect, url_for
from galeriaSM import app
from werkzeug.utils import secure_filename
from galeriaSM.forms import LoginForm, UploadForm
from config import settings
import os
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
    region_name = settings.AWS_REGION_NAME
)

bucket = settings.BUCKET


class Files():

    filenames = []
    login = False

    def get_login(self):
        return self.login

    def set_login(self, logged):
        self.login = logged

    def get_filenames(self):
        return self.filenames

    def set_filenames(self, names):
        self.filenames = names


f = Files()


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in settings.ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    files = []
    if request.method == "POST":
        selected = request.form.getlist('image')
        f.set_filenames(selected)
    else:
        selected = f.get_filenames()
    if not selected:
        flash("Nada a mostrar")
    for obj in selected:
        url = s3.generate_presigned_url('get_object',
                                        Params={
                                            'Bucket': bucket,
                                            'Key': obj
                                        },
                                        ExpiresIn=3600)
        files.append(url)
    return render_template('index.html', files=files, logged=f.get_login())


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        flash("Imagem salva")
        return redirect(url_for('upload'))
    return render_template('upload.html', title='Upload', form=form, logged=f.get_login())


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Seja bem vindo, {}!".format(
            form.username.data))
        f.set_login(True)
        return redirect(url_for('aprovacao'))
    return render_template('login.html', title='Sign In', form=form, logged=f.get_login())


@app.route('/logoff', methods=["GET", "POST"])
def logoff():
    flash("Usuário desconectado!")
    f.set_login(False)
    return render_template('index.html', title='Galeria', logged=f.get_login())


@app.route("/aprovacao", methods=["GET", "POST"])
def aprovacao():
    if f.get_login():
        files = {}
        cont = 0
        for obj in s3.list_objects_v2(Bucket=bucket)['Contents']:
            url = s3.generate_presigned_url('get_object',
                                            Params={
                                                'Bucket': bucket,
                                                'Key': obj['Key']
                                            },
                                            ExpiresIn=3600)
            files[cont] = {'name': obj['Key'], 'url': url}
            cont = cont + 1
        return render_template('aprovacao.html', title='Aprovação', files=files, logged=f.get_login())
    else:
        flash("Efetue login para aprovar fotos")
        return redirect(url_for('login'))
