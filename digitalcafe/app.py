from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
import database as db
import authentication
import ordermanagement as om
import logging

app = Flask(__name__)

# Set the secret key to some random bytes.
# Keep this really secret!
# Remove the "login" value (changepassword html)
# Remove the username --> It should read the session user
# What is type and name
app.secret_key = b's@g@d@c0ff33!'

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

navbar = """
        <a href='/'>Home</a> | <a href='/products'>Products</a> |
        <a href='/branches'>Branches</a> | <a href='/aboutus'>About Us</a>
        <p/>
        """

@app.route('/orderhistory')
def orderhistory():
    # equivalent code for find()
    return render_template('orderhistory.html')

@app.route('/checkout')
def checkout():
    # clear cart in session memory upon checkout
    om.create_order_from_cart()
    session.pop("cart",None)
    return redirect('/ordercomplete')

@app.route('/ordercomplete')
def ordercomplete():
    return render_template('ordercomplete.html')

@app.route('/addtocart',methods=['GET', 'POST'])
def addtocart():
    code = request.form.get('code', '')
    product = db.get_product(int(code))
    item=dict()
    # A click to add a product translates to a
    # quantity of 1 for now
    # item["qty"] = 1
    item["qty"] = int(request.form.get('qty','1'))
    item["name"] = product["name"]
    item["subtotal"] = product["price"]*item["qty"]

    if(session.get("cart") is None):
        session["cart"]={}

    cart = session["cart"]
    cart[code]=item
    session["cart"]=cart
    return redirect('/cart')

@app.route('/cart')
def cart():
    qty = request.form.getlist("qty")
    return render_template('cart.html',qty=qty)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/errorlogin', methods=['GET', 'POST'])
def errorlogin():
    return render_template('errorlogin.html')

@app.route('/auth', methods = ['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    app.logger.info('%s', is_successful)
    if(is_successful):
        session["user"] = user
        return redirect('/')
    else:
        return redirect('/errorlogin')

@app.route('/newpassword')
def newpassword():
        # check if the password matches what's in the database
        # import then call the function
        # similar to database and auth
        return redirect('/failedpasswordupdate')

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    return render_template('productdetails.html', code=code, product=product)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', page="Branches", branch_list=branch_list)

@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))
    return render_template('branchdetails.html', code=code, branch=branch)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/changepassword')
def changepassword():
    return render_template('changepassword.html')

@app.route('/failedpasswordupdate')
def failedpasswordupdate():
    return render_template('failedpasswordupdate.html')
