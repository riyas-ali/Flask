from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Type something in url after "/"'

@app.route('/<name>')
def home(name):
    return render_template('index.html', content=name, names=['Lenovo', 'MSI', 'Asus', 'Hp', 'Dell'])

@app.route('/admin')
def admin():
    return redirect(url_for('home', name='Admin'))

if __name__ == '__main__':
    app.run()
