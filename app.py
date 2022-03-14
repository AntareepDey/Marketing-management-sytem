from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
app = Flask(__name__)
  
# Configuring the database 
app.secret_key = 'hehe'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'userbase'
  
mysql = MySQL(app)

#setting the app routes  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():   # to handle login operations
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
  
@app.route('/logout')
def logout():    # to handle logout operations
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login/dashboard')
def dashboard():  # to show the dashboard
    return render_template('dashboard.html')

@app.route('/login/products')
def products():  #to show the products page
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    cur.close()
    return render_template('products.html', products=data )

@app.route('/login/products/insert_pro', methods =['POST'])
def insert_pro():       #insert records into the products table
    if request.method == "POST":
        flash("Data Inserted Successfully")
        pcode = request.form['pcode']
        name = request.form['name']
        price=request.form['price']
        stock=request.form['stock']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products(pcode,name,price,stock) VALUES (%s,%s,%s,%s)", (pcode,name,price,stock))
        mysql.connection.commit()
        return redirect(url_for('products'))  

@app.route('/login/products/update_pro',methods=['POST'])
def update_pro():           #update records from the products table
    if request.method == 'POST':
        pcode = request.form['pcode']
        name = request.form['name']
        price=request.form['price']
        stock=request.form['stock']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE products
               SET name=%s, price=%s,stock=%s
               WHERE pcode=%s
            """, (name,price,stock, pcode))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('products'))

@app.route('/login/products/delete_pro/<string:id_data>', methods = ['GET'])
def delete_pro(id_data):    #delete records from the products table
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE pcode=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('products'))

@app.route('/login/customers')
def customers():    #to show the customers page
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    data = cur.fetchall()
    cur.close()
    return render_template('customers.html', customers=data)

@app.route('/login/customers/insert_cus', methods =['POST'])
def insert_cus():       #insert record into the customers table
    if request.method == "POST":
        flash("Data Inserted Successfully")
        ccode = request.form['ccode']
        name = request.form['name']
        phno=request.form['phno']
        address=request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers(ccode,name,phno,address) VALUES (%s,%s,%s,%s)", (ccode,name,phno,address))
        mysql.connection.commit()
        return redirect(url_for('customers'))

@app.route('/login/customers/update_cus',methods=['POST'])
def update_cus():                    #update records from the customers table
    if request.method == 'POST':
        ccode = request.form['ccode']
        name = request.form['name']
        phno=request.form['phno']
        address=request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customers SET name=%s, phno=%s,address=%s WHERE ccode=%s", (name,phno,address,ccode))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('customers'))

@app.route('/login/customers/delete_cus/<string:id_data>', methods = ['GET'])
def delete_cus(id_data):        #delete records from the customers table
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE ccode=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('customers'))

@app.route('/login/employees')
def employees():        #to show the Employees page
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    cur.close()
    return render_template('employee.html',employees=data)

@app.route('/login/employees/insert_emp', methods =['POST'])
def insert_emp():               #insert record into the employees table
    if request.method == "POST":
        flash("Data Inserted Successfully")
        ecode = request.form['ecode']
        name = request.form['name']
        email=request.form['email']
        position=request.form['position']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees(ecode,name,email,position) VALUES (%s,%s,%s,%s)", (ecode,name,email,position))
        mysql.connection.commit()
        return redirect(url_for('employees'))

@app.route('/login/employees/update_emp',methods=['POST'])
def update_emp():                       #update records from the employee table
    if request.method == 'POST':
        ecode = request.form['ecode']
        name = request.form['name']
        email=request.form['email']
        position=request.form['position']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE employees
               SET name=%s, email=%s,position=%s
               WHERE ecode=%s
            """, (name,email,position,ecode))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('employees')) 

@app.route('/login/employees/delete_emp/<string:id_data>', methods = ['GET'])
def delete_emp(id_data):            #delete records from the employees table
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE ecode=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('employees'))               


@app.route('/login/orders')
def orders():                   #to show the orders page
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders")
    data = cur.fetchall()
    cur.close()
    return render_template('orders.html',orders=data)
     

@app.route('/login/orders/insert_ord', methods =['POST'])
def insert_ord():                #insert record into the orders table
    if request.method == "POST":
        flash("Data Inserted Successfully")
        ono = request.form['ono']
        pcode = request.form['pcode']
        ccode=request.form['ccode']
        bill=request.form['bill']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO orders(ono,pcode,ccode,bill) VALUES (%s,%s,%s,%s)", (ono,pcode,ccode,bill))
        mysql.connection.commit()
        return redirect(url_for('orders'))  

@app.route('/login/orders/update_ord',methods=['POST'])
def update_ord():                   #update records from the orders  table
    if request.method == 'POST':
        ono = request.form['ono']
        pcode = request.form['pcode']
        ccode=request.form['ccode']
        bill=request.form['bill']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE orders
               SET pcode=%s, ccode=%s,bill=%s
               WHERE ono=%s
            """, (pcode,ccode,bill,ono))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('orders'))  

@app.route('/login/orders/delete_ord/<string:id_data>', methods = ['GET'])
def delete_ord(id_data):     #delete records from the orders table
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM orders WHERE ono=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('orders'))                

@app.route('/login/outlets')
def outlets():                  #to show the Outlets page
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM outlets")
    data = cur.fetchall()
    cur.close()
    return render_template('outlets.html', outlets=data )
    

@app.route('/login/outlets/insert', methods =['POST'])
def insert():                       #insert record into the outlets table
    if request.method == "POST":
        flash("Data Inserted Successfully")
        location = request.form['location']
        revenue = request.form['revenue']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO outlets (location,revenue) VALUES (%s, %s)", (location, revenue))
        mysql.connection.commit()
        return redirect(url_for('outlets'))

@app.route('/login/outlets/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):            #delete records from the outlets table
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM outlets WHERE location=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('outlets'))

@app.route('/login/outlets/update',methods=['POST'])
def update():                    #update records from the outlets table
    if request.method == 'POST':
        location = request.form['location']
        revenue = request.form['revenue']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE outlets
               SET revenue=%s
               WHERE location=%s
            """, (revenue, location))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('outlets'))    
  
@app.route('/register', methods =['GET', 'POST'])
def register():                 # to handle the regitration operations
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

# to run the app
if __name__ == "__main__":
    app.run(debug=True)

    