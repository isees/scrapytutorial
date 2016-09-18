from flask import Flask, render_template, request, make_response, session, url_for, escape, redirect

app = Flask(__name__)

# >>> import os
# >>> os.urandom(24)
app.secret_key = '\xa3\xc8\xe8\xb7\xda\xbe\xa5\xc60D[b\x16\x91!\x128\xc1\xcb\x9ao\xad\xe9\x97'


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', name=escape(session['username']))
    return render_template('index.html')


@app.route('/user/<x>/<username>')
def show_user_profile(x, username):
    # show the user profile for that user
    return 'User %s %s' % (x, username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the  given id, the id is an integer
    return 'Post %d ' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


def valid_login(username, password):
    if username == 'bain' and password == '4':
        return True
    else:
        return False


def log_the_user_in(username):
    session['username'] = username
    resp = make_response(redirect(url_for('index')))
    # resp.set_cookie('username', username)
    resp.headers['X-Something'] = 'A value'
    return resp


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    info = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            # info = 'Login successfully!'
            return log_the_user_in(request.form['username'])
        else:
            info = 'Invalid username/password'
    return render_template('login.html', error=info)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
