from flask import render_template, flash, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from galeriasm import app, db
from werkzeug.utils import secure_filename
from werkzeug.urls import url_parse
from galeriasm.forms import LoginForm, UploadForm
from galeriasm.models import User, File
from config import settings
import os
import boto3

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION_NAME
)

bucket = settings.BUCKET


class Files():

    filenames = []

    def get_filenames(self):
        return File.query.filter_by(aprovada=True).all()

    def set_filenames(self, names):
        for filename in names:
            f = File.query.filter_by(name=filename).one()
            f.set_aprovada(True)


f = Files()


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in settings.ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "File": File}


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    files = []
    if request.method == "POST":
        selected = request.form.getlist("image")
        for filename in selected:
            img = File.query.filter_by(name=filename).one()
            img.set_aprovada(True)    
    aprovadas = f.get_filenames()
    if not aprovadas:
        flash("Nenhuma imagem aprovada")
    for obj in aprovadas:
        url = s3.generate_presigned_url("get_object",
                                        Params={
                                            "Bucket": bucket,
                                            "Key": obj.name
                                        },
                                        ExpiresIn=3600)
        files.append(url)
    return render_template("index.html", files=files)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        image = request.files["image"]
        filename = secure_filename(image.filename)
        s3.upload_fileobj(image, bucket, filename)
        f = File(name=filename)
        db.session.add(f)
        db.session.commit()
        saved_files = File.query.all()
        for sf in saved_files:
            print(sf.name)
        flash("Imagem salva")
        return redirect(url_for("upload"))
    return render_template("upload.html", title="Upload", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Usuário já autenticado!")
        return redirect(url_for("aprovacao"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Usuário e/ou senha inválidos!")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('aprovacao')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/aprovacao", methods=["GET", "POST"])
def aprovacao():
    if current_user.is_authenticated:
        for f in File.query.all():
            f.set_aprovada(False)  
        files = {}
        cont = 0
        saved_files = File.query.all()
        for sf in saved_files:
            url = s3.generate_presigned_url("get_object",
                                            Params={
                                                "Bucket": settings.BUCKET,
                                                "Key": sf.name
                                            },
                                            ExpiresIn=3600)
            files[cont] = {"name": sf.name, "url": url}
            cont = cont + 1
        return render_template("aprovacao.html", title="Aprovação", files=files)
    else:
        flash("Usuário não autenticado")
        return redirect(url_for("login"))
