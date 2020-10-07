from flask import render_template
from galeriaSM import app

@app.route('/')
@app.route('/index')
def index():
    pics = {'https://assets.vogue.com/photos/5dfbb1d1e3e1b20009a63674/16:9/w_1200%2Cc_limit/e%26t-wedding-523.jpg', 'https://i.insider.com/5e2762f7ab49fd1ed25a9dc4?width=1100&format=jpeg&auto=webp', 'https://cdn0.weddingwire.com/articles/images/5/8/9/5/img_5985/t30_rw-plan-a-wedding-step-by-step-porterhouse-los-angeles.jpeg', 'https://images.squarespace-cdn.com/content/5e8734078136f513e25d34c4/1586886099769-FUIR9U8C5M6U274RA4H8/Beach+Wedding+Crim+Barefoot+Beach+Bride+%282%29.jpg?content-type=image%2Fjpeg'}
    return render_template('index.html', title='Galeria', pics=pics)