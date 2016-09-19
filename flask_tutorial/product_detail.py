# coding: utf-8

from flask import Flask, render_template, request, make_response, session, url_for, escape, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from shimano_orm import Shimano
import json
import ast

image_host = 'http://www.shimano-china.com'

app = Flask(__name__)
app.secret_key = '\xa3\xc8\xe8\xb7\xda\xbe\xa5\xc60D[b\x16\x91!\x128\xc1\xcb\x9ao\xad\xe9\x97'


@app.route('/product/detail', methods=['POST', 'GET'])
def product_detail():
    model = request.args['model']
    result = Shimano.query.filter(Shimano.fitting_model == model).first()
    image_standard = image_host + result.fitting_image_standard
    fitting_class = result.fitting_class
    fitting_series = result.fitting_series
    fitting_features = result.fitting_features
    fitting_attributes = result.fitting_attributes
    features = ast.literal_eval(fitting_features)
    # for feature in features:
    #     print feature
    attributes = json.loads(fitting_attributes)
    return render_template('product_detail.html', name=result.name, fitting_model=result.fitting_model,
                           fitting_class=fitting_class,
                           fitting_series=fitting_series,
                           fitting_features=features,
                           fitting_attributes=attributes,
                           fitting_image_standard=image_standard)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
