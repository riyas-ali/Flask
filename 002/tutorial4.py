from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')


@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 