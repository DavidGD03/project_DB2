from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
from flask_uploads import UploadSet, configure_uploads, IMAGES
import timeit
import datetime
from flask_mail import Mail, Message
import os
from wtforms.fields.html5 import EmailField

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/image/product'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(app)


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('index'))
        else:
            return f(*args, *kwargs)

    return wrap


def is_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('admin_login'))

    return wrap


def not_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return redirect(url_for('admin'))
        else:
            return f(*args, *kwargs)

    return wrap


def wrappers(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped





@app.route('/')
def index():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    cur4 = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM objeto WHERE fk_id_categoria=1 ORDER BY RAND()")
    tecnologia = cur.fetchall()
    cur2.execute("SELECT * FROM objeto WHERE fk_id_categoria=2 ORDER BY RAND()")
    electro = cur2.fetchall()
    cur3.execute("SELECT * FROM objeto WHERE fk_id_categoria=3 ORDER BY RAND()")
    moda = cur3.fetchall()
    cur4.execute("SELECT * FROM objeto WHERE fk_id_categoria=4 ORDER BY RAND()")
    libros = cur4.fetchall()
    # Close Connection
    cur.close()
    return render_template('home.html', tecnologia=tecnologia, electro=electro, moda=moda, libros=libros, form=form)


class LoginForm(Form):  # Create Login Form
    username = StringField('', [validators.length(min=1)],
                           render_kw={'autofocus': True, 'placeholder': 'Usuario'})
    password = PasswordField('', [validators.length(min=3)],
                             render_kw={'placeholder': 'Contraseña'})



@app.route('/noticias')
def noticia():
    form = OrderForm(request.form)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM noticia")
    noticia = cur.fetchall()
    cur.close()
    if 'view' in request.args:
        q = request.args['view']
        product_id = q
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM noticia WHERE id=%s", (q,))
        objeto = curso.fetchall()
        return render_template('noticia_view.html', noticia=objeto)
    return render_template('noticias.html', noticia=noticia)



userid = ' '
useremail = ' '
# User Login
@app.route('/login', methods=['GET', 'POST'])
@not_logged_in
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # GEt user form
        username = form.username.data
        # password_candidate = request.form['password']
        password_candidate = form.password.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM usuario WHERE nickname=%s", [username])

        if result > 0:
            # Get stored value
            global userid
            global useremail
            data = cur.fetchone()
            password = data['contrasena']
            uid = data['id']
            emailid = data['correo']
            userid = uid
            useremail=emailid
            name = data['nombre']

            # Compare password
            if sha256_crypt.verify(password_candidate, password):
                # passed
                session['logged_in'] = True
                session['uid'] = uid
                session['s_name'] = name

                return redirect(url_for('index'))

            else:
                flash('Clave incorrecta', 'danger')
                return render_template('login.html', form=form)

        else:
            flash('Usuario no encontrado', 'danger')
            # Close connection
            cur.close()
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/out')
def logout():
    if 'uid' in session:
        # Create cursor
        session.clear()
        flash('Saliste de la sesión correct7amente', 'success')
        return redirect(url_for('index'))
    return redirect(url_for('login'))


class RegisterForm(Form):
    nombre = StringField('', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': 'Inserte su nombre'})
    nickname = StringField('', [validators.length(min=3, max=25)], render_kw={'placeholder': 'Inserte su nickname'})
    email = EmailField('', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Inserte su correo'})
    contrasena = PasswordField('', [validators.length(min=3)],
                             render_kw={'placeholder': 'Digite su contraseña'})
    telefono = StringField('', [validators.length(min=10, max=10)], render_kw={'placeholder': 'Inserte su telefono'})
    fchnacimiento = StringField('', [validators.DataRequired()], render_kw={'placeholder': 'Año-Mes-Día'})
    genero = StringField('', [validators.DataRequired(), validators.length(min=5)], render_kw={'placeholder': 'Genero'})
    departamento = StringField('', [validators.DataRequired(), validators.length(min=5)], render_kw={'placeholder': 'Departamento'})
    ciudad = StringField('', [validators.DataRequired(), validators.length(min=5)], render_kw={'placeholder': 'Digite su ciudad'})
    direccion = StringField('', [validators.DataRequired(), validators.length(min=6)], render_kw={'placeholder': 'Digite su dirección'})
    codpostal = StringField('', [validators.DataRequired(), validators.length(min=3)], render_kw={'placeholder': 'Digite su Codigo Postal'})




@app.route('/register', methods=['GET', 'POST'])
@not_logged_in
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        email = form.email.data
        nickname = form.nickname.data
        contrasena = sha256_crypt.encrypt(str(form.contrasena.data))
        telefono = form.telefono.data
        fchnacimiento = form.fchnacimiento.data
        genero = form.genero.data
        departamento = form.departamento.data
        ciudad = form.ciudad.data
        direccion = form.direccion.data
        codpostal = form.codpostal.data
        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario(nombre, correo, nickname, contrasena, telefono, genero, fchnacimiento, departamento, ciudad, direccion, codpostal) VALUES(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)",
                    (nombre, email, nickname, contrasena, telefono, genero, fchnacimiento, departamento, ciudad, direccion, codpostal))

        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Te has registrado correctamente y ahora puedes ingresar', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)



class MessageForm(Form):  # Create Message Form
    body = StringField('', [validators.length(min=1)], render_kw={'autofocus': True})





class OrderForm(Form):  # Create Order Form
    quantity = SelectField('', [validators.DataRequired()],
                           render_kw={'placeholder': 'Cantidad'})
    order_place = StringField('', [validators.length(min=1), validators.DataRequired()],
                              render_kw={'placeholder': 'Order Place'})


c1 = ' '
@app.route('/tecnologia', methods=['GET', 'POST'])
def tecnologia():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM objeto WHERE fk_id_categoria=1")
    tecnologia = cur.fetchall()
    # Close Connection
    cur.close()
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (product_id,))
        tecnologia = curso.fetchall()
        categoria = 'tecnologia'
        if 'uid' in session:
            uid = session['uid']
        return render_template('view_product.html', tecnologia=tecnologia,categoria=categoria)
    elif 'order' in request.args:
        global useremail, userid
        product_id = request.args['order']
        cur2 = mysql.connection.cursor()
        cur2.execute("INSERT INTO carrito (idusuario, correousuario,idobjeto) VALUES (%s, %s, %s)", (userid,useremail,product_id))
        mysql.connection.commit()
        cur2.close()
        categoria = 'tecnologia'
        flash('Producto añadido a la cesta', 'success')
        return render_template('tecnologia.html', categoria=categoria)
    return render_template('tecnologia.html', tecnologia=tecnologia, form=form)


@app.route("/carrito")
def carrito():
    global userid
    cur = mysql.connection.cursor()
    cur.execute("SELECT objeto.id, objeto.nombre, objeto.precio FROM objeto, carrito WHERE objeto.id = carrito.idobjeto AND carrito.idusuario = %s", (userid, ))
    products = cur.fetchall()
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT sum(objeto.precio) FROM objeto, carrito WHERE objeto.id = carrito.idobjeto AND carrito.idusuario = %s", (userid, ))
    preciototal = cur2.fetchall()
    return render_template("carrito.html", products = products, preciototal = preciototal)

@app.route("/quitarcarrito")
def quitarcarrito():
    global userid
    productId = int(request.args.get('productId'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM carrito WHERE idusuario = %s AND idobjeto = %s", (userid, productId))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('carrito'))

@app.route('/electro', methods=['GET', 'POST'])
def electro():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM objeto WHERE fk_id_categoria=2 ORDER BY id ASC")
    objeto = cur.fetchall()
    # Close Connection
    cur.close()

    if request.method == 'POST' and form.validate():
        name = form.name.data
        mobile = form.mobile_num.data
        order_place = form.order_place.data
        quantity = form.quantity.data
        pid = request.args['order']

        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            curs.execute("INSERT INTO orden(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                         (uid, pid, name, mobile, order_place, quantity, now_time))
        else:
            curs.execute("INSERT INTO orden(pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s)",
                         (pid, name, mobile, order_place, quantity, now_time))
        # Commit cursor
        mysql.connection.commit()
        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('electro.html', electro=objeto, form=form)
    if 'view' in request.args:
        q = request.args['view']
        product_id = q
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (q,))
        objeto = curso.fetchall()
        return render_template('view_product.html',  tecnologia=objeto)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (product_id,))
        product = curso.fetchall()
        return render_template('order_product.html', tecnologia=product, form=form)
    return render_template('electro.html', electro=objeto, form=form)


@app.route('/moda', methods=['GET', 'POST'])
def moda():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM objeto WHERE fk_id_categoria=3 ORDER BY id ASC")
    objeto = cur.fetchall()
    # Close Connection
    cur.close()

    if request.method == 'POST' and form.validate():
        name = form.name.data
        mobile = form.mobile_num.data
        order_place = form.order_place.data
        quantity = form.quantity.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            curs.execute("INSERT INTO orden(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                         (uid, pid, name, mobile, order_place, quantity, now_time))
        else:
            curs.execute("INSERT INTO orden(pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s)",
                         (pid, name, mobile, order_place, quantity, now_time))

        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('moda.html', moda=objeto, form=form)
    if 'view' in request.args:
        q = request.args['view']
        product_id = q
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (q,))
        objeto = curso.fetchall()
        return render_template('view_product.html', tecnologia=objeto)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (product_id,))
        product = curso.fetchall()
        return render_template('order_product.html', tecnologia=product, form=form)
    return render_template('moda.html', moda=objeto, form=form)


@app.route('/libros', methods=['GET', 'POST'])
def libros():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM objeto WHERE fk_id_categoria=4 ORDER BY id ASC")
    objeto = cur.fetchall()
    # Close Connection
    cur.close()

    if request.method == 'POST' and form.validate():
        name = form.name.data
        mobile = form.mobile_num.data
        order_place = form.order_place.data
        quantity = form.quantity.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            curs.execute("INSERT INTO orden(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                         (uid, pid, name, mobile, order_place, quantity, now_time))
        else:
            curs.execute("INSERT INTO orden(pid, ofname, mobile, oplace, quantity, ddate) "
                         "VALUES(%s, %s, %s, %s, %s, %s)",
                         (pid, name, mobile, order_place, quantity, now_time))
        # Commit cursor
        mysql.connection.commit()
        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('libros.html', libros=objeto, form=form)
    if 'view' in request.args:
        q = request.args['view']
        product_id = q
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (q,))
        objeto = curso.fetchall()
        return render_template('view_product.html',  tecnologia=objeto)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM objeto WHERE id=%s", (product_id,))
        product = curso.fetchall()
        return render_template('order_product.html',  tecnologia=product, form=form)
    return render_template('libros.html', libros=objeto, form=form)

adminid = ' '
@app.route('/admin_login', methods=['GET', 'POST'])
@not_admin_logged_in
def admin_login():
    if request.method == 'POST':
        global adminid 
        username = request.form['email']
        password_candidate = request.form['password']


        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM empleado WHERE email=%s", [username])

        if result > 0:    
            data = cur.fetchone()
            password = data['password']
            uid = data['id']
            adminid = uid
            name = data['nombrec']

  
            if sha256_crypt.verify(password_candidate, password):

                session['admin_logged_in'] = True
                session['admin_uid'] = uid
                session['admin_name'] = name

                return redirect(url_for('admin'))

            else:
                flash('Clave incorrecta', 'danger')
                return render_template('pages/login.html')

        else:
            flash('Nombre de usuario no encontrado', 'danger')
            cur.close()
            return render_template('pages/login.html')
    return render_template('pages/login.html')


@app.route('/admin_out')
def admin_logout():
    if 'admin_logged_in' in session:
        session.clear()
        return redirect(url_for('admin_login'))
    return redirect(url_for('admin'))


@app.route('/admin')
@is_admin_logged_in
def admin():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM objeto")
    result = curso.fetchall()
    order_rows = curso.execute("SELECT * FROM orden")
    usuario_rows = curso.execute("SELECT * FROM usuario")
    return render_template('pages/index.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=usuario_rows)

@app.route('/admin_ver_reclamo')
@is_admin_logged_in
def admin_reclamo():
    curso = mysql.connection.cursor()
    curso.execute("SELECT * FROM reclama")
    result = curso.fetchall()
    return render_template('pages/reclamos.html', result=result)


@app.route('/orders')
@is_admin_logged_in
def orden():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM objeto")
    order_rows = curso.execute("SELECT * FROM orden")
    result = curso.fetchall()
    usuario_rows = curso.execute("SELECT * FROM usuario")
    return render_template('pages/all_orders.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=usuario_rows)


@app.route('/users')
@is_admin_logged_in
def usuario():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM objeto")
    order_rows = curso.execute("SELECT * FROM orden")
    usuario_rows = curso.execute("SELECT * FROM usuario")
    result = curso.fetchall()
    return render_template('pages/all_users.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=usuario_rows)


@app.route('/admin_add_product', methods=['POST', 'GET'])
@is_admin_logged_in
def admin_add_product():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        fk_id_categoria = request.form['fk_id_categoria']
        garantia = request.form['garantia']
        empresa = request.form['empresa']
        file = request.files['imagen']
        if nombre and precio and descripcion and cantidad and fk_id_categoria and garantia and empresa and file:
            pic = file.filename
            photo = pic.replace("'", "")
            picture = photo.replace(" ", "_")
            if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                save_photo = photos.save(file, folder=fk_id_categoria)
                if save_photo:
                    curs = mysql.connection.cursor()
                    curs.execute("INSERT INTO objeto(nombre,precio,descripcion,cantidad,fk_id_categoria,garantia,fk_id_empresa,imagen)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                 (nombre,precio,descripcion,cantidad,fk_id_categoria,garantia,empresa,picture))
                    mysql.connection.commit()
                    cur2 = mysql.connection.cursor()
                    cur2.execute("SELECT * FROM objeto WHERE nombre=%s", [nombre])
                    idf = cur2.fetchone()
                    curs.execute("INSERT INTO pertenece(id_categoria,id_objeto)"
                                "VALUES (%s, %s)",
                                (fk_id_categoria, idf['id']))
                    mysql.connection.commit()
                    curs.close()

                    flash('Producto añadido correctamente', 'success')
                    return redirect(url_for('admin_add_product'))
                else:
                    flash('Imagen no guardada', 'danger')
                    return redirect(url_for('admin_add_product'))
            else:
                flash('Archivo no soportado', 'danger')
                return redirect(url_for('admin_add_product'))
        else:
            flash('Por favor rellene todo el formulario', 'danger')
            return redirect(url_for('admin_add_product'))
    else:
        return render_template('pages/add_product.html')


@app.route('/edit_product', methods=['POST', 'GET'])
@is_admin_logged_in
def edit_product():
    if 'id' in request.args:
        objeto_id = request.args['id']
        curso = mysql.connection.cursor()
        res = curso.execute("SELECT * FROM objeto WHERE id=%s", [objeto_id])
        carpeta = 'objeto'
        objeto = curso.fetchall()
        if res > 0:
            if request.method == 'POST':
                nombre = request.form.get('nombre')
                precio = request.form['precio']
                descripcion = request.form['descripcion']
                cantidad = request.form['cantidad']
                fk_id_categoria = request.form['fk_id_categoria']
                garantia = request.form['garantia']
                empresa = request.form['fk_id_empresa']
                file = request.files['picture']
                # Create Cursor
                if nombre and precio and descripcion and cantidad and fk_id_categoria and garantia and empresa and file:
                    pic = file.filename
                    photo = pic.replace("'", "")
                    picture = photo.replace(" ", "_")
                    if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                        save_photo = photos.save(file, folder=carpeta)
                        if save_photo:
                            curso.execute(
                            "UPDATE objeto SET nombre=%s, precio=%s, descripcion=%s, cantidad=%s, fk_id_categoria=%s, garantia=%s, fk_id_empresa=%s, imagen=%s WHERE id=%s",
                            (nombre, precio, descripcion, cantidad, fk_id_categoria, garantia, empresa, pic, objeto_id))
                            # Commit cursor
                            mysql.connection.commit()
                            curso.close()
                            flash('Objeto actualizado', 'success')
                            return redirect(url_for('edit_product'))
                
                        else:
                            flash('Imagen no subida', 'danger')
                            return render_template('pages/edit_product.html', objeto=objeto)
                    else:
                        flash('Archivo no soportado', 'danger')
                        return render_template('pages/edit_product.html', objeto=objeto)
                else:
                    flash('Rellena todos los campos', 'danger')
                    return render_template('pages/edit_product.html', objeto=objeto)
            else:
                print('get')
                return render_template('pages/edit_product.html', objeto=objeto)
        else:
            return redirect(url_for('admin_login'))
    else:
        return redirect(url_for('admin_login'))

@app.route('/admin_add_empleado', methods=['POST', 'GET'])
@is_admin_logged_in
def admin_add_empleado():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono1 = request.form['telefono1']
        cedula = request.form['cedula']
        telefono2 = request.form['telefono2']
        correo = request.form['correo']
        genero = request.form['genero']
        fcnacimiento = request.form['fcnacimiento']
        contrasena = sha256_crypt.encrypt(str(request.form['contrasena']))
        if nombre and telefono1 and correo and genero and fcnacimiento:
                
               
             # Create Cursor
             curs = mysql.connection.cursor()
             curs.execute("INSERT INTO empleado(id,nombrec,password,telefono,email,genero,telefono2,fchnacimiento)"
                          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                         (cedula,nombre,contrasena,telefono1,correo,genero,telefono2,fcnacimiento))
             mysql.connection.commit()
             # Close Connection
             curs.close()

             flash('Product added successful', 'success')
             return redirect(url_for('admin_add_empleado'))
        else:
            flash('Please fill up all form', 'danger')
            return redirect(url_for('admin_add_empleado'))
    else:
        return render_template('pages/add_empleado.html')


@app.route('/admin_add_new', methods=['POST', 'GET'])
@is_admin_logged_in
def admin_add_new():
    ## ida = session['admin_uid']
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        file = request.files['picture']
        carpeta = 'noticia'
        if titulo and descripcion and fecha and file:
            pic = file.filename
            photo = pic.replace("'", "")
            picture = photo.replace(" ", "_")
            if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                save_photo = photos.save(file, folder=carpeta)
                if save_photo:
                    # Create Cursor
                    curs = mysql.connection.cursor()
                    curs.execute("INSERT INTO noticia(titulo,descripcion,fecha,imagen,fk_id_empleado)"
                                 "VALUES(%s, %s, %s, %s,%s)",
                                 (titulo,descripcion,fecha,picture,adminid))
                    mysql.connection.commit()
                    # Close Connection
                    curs.close()

                    flash('Noticia agregada satisfactoriamente', 'success')
                    return redirect(url_for('admin_add_new'))
                else:
                    flash('Imagen no guardada', 'danger')
                    return redirect(url_for('admin_add_new'))
            else:
                flash('Archivo no soportado', 'danger')
                return redirect(url_for('admin_add_new'))
        else:
            flash('Por favor rellene todo el formulario', 'danger')
            return redirect(url_for('admin_add_new'))
    else:
        return render_template('pages/add_new.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    form = OrderForm(request.form)
    if 'q' in request.args:
        q = request.args['q']
        # Create cursor
        cur = mysql.connection.cursor()
        # Get message
        query_string = "SELECT * FROM objeto WHERE nombre LIKE %s ORDER BY id ASC"
        cur.execute(query_string, ('%' + q + '%',))
        objeto = cur.fetchall()
        # Close Connection
        cur.close()
        flash('Mostrando resultados para: ' + q, 'success')
        return render_template('search.html', objeto=objeto, form=form)
    else:
        flash('Busca de nuevo', 'danger')
        return render_template('search.html')


@app.route('/reclamos', methods=['POST', 'GET'])
@is_logged_in
def add_reclamo():
    ## ida = session['admin_uid']
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form['descripcion']
        objeto = request.form['fk_id_objeto']
        if titulo and descripcion and objeto:
            
            curs = mysql.connection.cursor()
            curs.execute("INSERT INTO reclama(titulo,descripcion,fk_id_objeto,fk_id_usuario,fk_correo)"
                        "VALUES(%s, %s, %s, %s,%s)",
                        (titulo,descripcion,objeto,userid,useremail))
            mysql.connection.commit()
            # Close Connection
            curs.close()
            flash('Reclamo hecho satisfactoriamente', 'success')
            return redirect(url_for('add_reclamo'))
        else:
            flash('Por favor rellene todo el formulario', 'danger')
            return redirect(url_for('add_reclamo'))
    else:
        return render_template('/reclamo.html')

@app.route('/profile')
@is_logged_in
def profile():
    if 'user' in request.args:
        q = request.args['user']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM usuario WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                curso.execute("SELECT * FROM orden WHERE id=%s ORDER BY id ASC", (session['uid'],))
                res = curso.fetchall()
                return render_template('profile.html', result=res)
            else:
                flash('No está autorizado, por favor ingrese con su usuario', 'danger')
                return redirect(url_for('login'))
        else:
            flash('UNo está autorizado, por favor ingrese con su usuario', 'danger')
            return redirect(url_for('login'))
    else:
        flash('No autorizado', 'danger')
        return redirect(url_for('login'))


class UpdateRegisterForm(Form):
    name = StringField('Nombre completo', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': 'Nombre Completo'})
    email = EmailField('Email', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Email'})
    password = PasswordField('Contraseña', [validators.length(min=3)],
                             render_kw={'placeholder': 'Contraseña'})
    mobile = StringField('Telefono', [validators.length(min=11, max=15)], render_kw={'placeholder': 'Telefono'})


@app.route('/settings', methods=['POST', 'GET'])
@is_logged_in
def settings():
    form = UpdateRegisterForm(request.form)
    if 'user' in request.args:
        q = request.args['user']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM usuario WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                if request.method == 'POST' and form.validate():
                    name = form.name.data
                    email = form.email.data
                    password = sha256_crypt.encrypt(str(form.password.data))
                    mobile = form.mobile.data

                    # Create Cursor
                    cur = mysql.connection.cursor()
                    exe = cur.execute("UPDATE usuario SET name=%s, email=%s, password=%s, mobile=%s WHERE id=%s",
                                      (name, email, password, mobile, q))
                    if exe:
                        flash('Profile updated', 'success')
                        return render_template('user_settings.html', result=result, form=form)
                    else:
                        flash('Profile not updated', 'danger')
                return render_template('user_settings.html', result=result, form=form)
            else:
                flash('Unauthorised', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Unauthorised! Please login', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Unauthorised', 'danger')
        return redirect(url_for('login'))


class BuscarForm(Form):  #
    id = StringField('', [validators.length(min=1)],
                     render_kw={'placeholder': 'Ingresa el nombre de un producto...'})




if __name__ == '__main__':
    app.run(debug=True)
