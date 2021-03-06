from flask import Flask
from flask import Request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'goodbye, World!'

@app.route('/uploadImage', methods=['GET','POST'])
def upload_img():
    if request.method == 'POST':
        f = request.files['product_img']
        f.save('/var/www/uploads/product_img.jpg')
        return 'image uploaded!'
    return 'image not uploaded...'