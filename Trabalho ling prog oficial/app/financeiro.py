from flask import Flask, render_template, request, redirect, url_for ,flash
from flask_login import login_user , current_user , logout_user, login_required
from app.forms import LoginForm, RegisterForm
from app.tables import User
from app.webscrapping import poupanca, fundos, acoes, dolar_cambio, euro_cambio
from app import app, db, lm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])
def begin():
    if request.method == 'POST':
        pass
    return render_template('index.html')


@app.route('/signin', methods = ["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('homepage'))
    return render_template('form.html', form=form)

@app.route('/logout', methods = ['POST', 'GET'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
    return redirect(url_for('begin'))

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        try:
            NewUserData = User(form.username.data,form.password.data)
            db.session.add(NewUserData)
            db.session.commit()
            return redirect(url_for("signin"))
        except:
            return redirect(url_for("register"))
    return render_template('registro.html', form=form)


@app.route('/home',methods=['POST', 'GET'])
@login_required
def homepage():
        return render_template('homepage.html')

@app.route('/dolar', methods=['POST', 'GET'])
@login_required
def dolar(dolar_moeda = None):
    if request.method == 'POST':
        dinheiro = dolar_cambio()
        return render_template('dolar.html', dolar_moeda = dinheiro.get_dolar())

@app.route('/euro', methods=['POST', 'GET'])
@login_required
def euro(euro_moeda = None):
    if request.method == 'POST':
        dinheiro = euro_cambio()
        return render_template('euro.html', euro_moeda = dinheiro.get_euro())

@app.route('/calculo_investimento', methods=['POST', 'GET'])
@login_required
def calc_inv(poup = None, ifix = None, ibovespa = None):
    if request.method == 'POST':
        valor_poupanca = poupanca()
        valor_ifix = fundos()
        valor_ibovespa = acoes()
        return render_template('calc_inv.html', poup = valor_poupanca.get_poupanca(), 
                               ifix = valor_ifix.get_fundos(), ibovespa = valor_ibovespa.get_acoes())




    