import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/scan_all')
def render_scan_all():
    return render_template("scan-all.html")

@app.route('/scan_safe')
def render_scan_safe():
    return render_template("scan-safe.html")

@app.route('/scan_unsafe')
def render_scan_unsafe():
    return render_template("scan-unsafe.html")

@app.route('/ingredients')
def render_ingredients():
    return render_template("ingredient.html")

@app.route('/', methods=['GET','POST'])
def upload_img():
    # print ('upload image called')
    # app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # if request.method == 'POST':
    #     print ('in POST')
    #     img = request.files['file']
    #     print ('received image')
    #     # img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename)))
    #     print ('saved image')
    #     return redirect(url_for('render_scan_safe'))
    print ('ok whatever redirect then')
    return redirect(url_for('render_scan_safe'))