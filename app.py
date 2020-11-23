from flask import *
from models.user import User
from models.product import Product
import service
import db

app = Flask(__name__)
app.secret_key = "suachua"
db.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gioithieu')
def about():
    return render_template('gioithieu.html')

@app.route('/product')
def product():
    all_products = service.get_display_product()
    return render_template('product.html', all_products=all_products)

@app.route('/tintuc')
def tintuc():
    return render_template('tintuc.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    
    res = service.validate_user(email, password)
  
    if res:
        session['user-loggedin'] = True
        session["user_id"] = str(res.id)
        session["user-name"] = res.lastname + " " + res.firstname
        return jsonify({
            'success': True,
            'user_id':str(res.id),
            'email':res.email, 
            'role':res.role,
            'firstname':res.firstname, 
            'lastname':res.lastname, 
            'phone':res.phone
        }) , 200
    else: 
        return jsonify({'success': False}), 200

@app.route('/logout')
def logout():
    if session['user-loggedin'] == False:
        return redirect(url_for('index'))
    else:
        session['user-loggedin'] = False
        del session["user_id"]
        del session["user-name"]
        return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    phone = request.json['phone']

    res = service.create_user(email, password, firstname, lastname, phone)
    if res:
        return jsonify({
        'success': True
        }) , 200
    else: 
        return jsonify({
        'success': False,
        'error' : 'invalid email'
        }), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug= True)