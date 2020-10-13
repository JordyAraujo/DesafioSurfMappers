from flask import render_template, flash, request, redirect, url_for
from galeriaSM import app
from werkzeug.utils import secure_filename
from galeriaSM.login import LoginForm
import os
import boto3

s3 = boto3.client('s3')
bucket = 'galeriasmbucket'


class Files():

    filenames = []

    def get_filenames(self):
        return self.filenames

    def set_filenames(self, names):
        self.filenames = names


f = Files()


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
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
    return render_template('index.html', files=files)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                flash('No filename')
                return redirect(url_for('upload'))
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                s3.upload_fileobj(image, 'galeriasmbucket', filename)
                flash("Imagem salva")
                return redirect(url_for('index'))
            else:
                flash("Formato de arquivo não permitido")
                return redirect(url_for('upload'))
    return render_template("upload.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Seja bem vindo, {}!".format(
            form.username.data))
        return redirect('/aprovacao')
    return render_template('login.html', title='Sign In', form=form)


@app.route("/aprovacao", methods=["GET", "POST"])
def aprovacao():
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
    return render_template('aprovacao.html', title='Aprovação', files=files)
