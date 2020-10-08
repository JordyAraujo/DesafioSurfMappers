from flask import render_template, request, redirect, jsonify, send_from_directory
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
    pics = {'https://assets.vogue.com/photos/5dfbb1d1e3e1b20009a63674/16:9/w_1200%2Cc_limit/e%26t-wedding-523.jpg', 'https://i.insider.com/5e2762f7ab49fd1ed25a9dc4?width=1100&format=jpeg&auto=webp',
            'https://cdn0.weddingwire.com/articles/images/5/8/9/5/img_5985/t30_rw-plan-a-wedding-step-by-step-porterhouse-los-angeles.jpeg', 'https://images.squarespace-cdn.com/content/5e8734078136f513e25d34c4/1586886099769-FUIR9U8C5M6U274RA4H8/Beach+Wedding+Crim+Barefoot+Beach+Bride+%282%29.jpg?content-type=image%2Fjpeg'}
    return render_template('index.html', title='Galeria', pics=pics)


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
                image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
                print("Imagem salva")
                return redirect(request.url)
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