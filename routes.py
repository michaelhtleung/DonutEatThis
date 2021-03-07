import data_pipeline as dp

from flask import Flask
import os

app = Flask(__name__)


@app.route('/uploadImage')
def uploadImage():
    # The name of the image file to annotate
    path = os.path.abspath('hashbrowns_ingredients.jpeg')
    content = None
    # payload = dp.process_image(path=path, content=content)
    # return payload
    return 'goodbye world!'
