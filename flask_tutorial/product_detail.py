from flask import Flask, render_template, request, make_response, session, url_for, escape, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import shimano_orm

app = Flask(__name__)
app.secret_key = '\xa3\xc8\xe8\xb7\xda\xbe\xa5\xc60D[b\x16\x91!\x128\xc1\xcb\x9ao\xad\xe9\x97'


@app.route('/product/detail', methods=['POST', 'GET'])
def product_detail():
    model = request.args['model']
    # if request.method == 'POST':
    #     model = request.get_data('model')
    #     model = request.get_data('model')
    return render_template('product_detail.html', fitting_model=model)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
