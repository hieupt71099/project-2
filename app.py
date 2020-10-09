from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gioithieu')
def about():
    return render_template('gioithieu.html')

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug= True)