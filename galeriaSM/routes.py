from flask import render_template, request, redirect, url_for
from galeriaSM import app
from werkzeug.utils import secure_filename
import os
import boto3

s3 = boto3.client('s3')
bucket = 'galeriasmbucket'


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
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(url_for('index'))
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                s3.upload_fileobj(image, 'galeriasmbucket', filename)
                print("Imagem salva")
                return redirect(url_for('aprovacao'))
            else:
                print("Formato de arquivo não permitido")
                return redirect(redirect.url)
    return render_template("index.html")


@app.route("/aprovacao", methods=["GET", "POST"])
def aprovacao():
    files = []
    names = []
    for obj in s3.list_objects_v2(Bucket=bucket)['Contents']:
        url = s3.generate_presigned_url('get_object',
                                        Params={
                                            'Bucket': bucket,
                                            'Key': obj['Key']
                                        },
                                        ExpiresIn=3600)
        files.append(url)
        names.append(obj['Key'])
    return render_template('aprovacao.html', title='Aprovação', files=files, names=names)

@app.route("/galeria", methods=["GET", "POST"])
def galeria():
    files = []
    if request.method == "POST":
        filenames = request.form.getlist('image')
    for obj in filenames:
        url = s3.generate_presigned_url('get_object',
                                        Params={
                                            'Bucket': bucket,
                                            'Key': obj
                                        },
                                        ExpiresIn=3600)
        files.append(url)
    return render_template('galeria.html', files=files)