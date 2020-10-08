from flask import render_template, request, redirect, jsonify, send_from_directory, url_for
from galeriaSM import app
from werkzeug.utils import secure_filename
import os


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False


@app.route('/')
@app.route('/index')
def index():
    files = []
    for filename in os.listdir(app.config["UPLOAD_FOLDER"]):
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        if os.path.isfile(path):
            files.append(filename)
    return render_template('index.html', title='Galeria', files=files)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(
                    app.config["UPLOAD_FOLDER"], image.filename))
                print("Imagem salva")
                return redirect(url_for('index'))
            else:
                print("Formato de arquivo não permitido")
                return redirect(redirect.url)
    return render_template("upload.html")


@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(app.config["UPLOAD_FOLDER"]):
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], path, as_attachment=True)
