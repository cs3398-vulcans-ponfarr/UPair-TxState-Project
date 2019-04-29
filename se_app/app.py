from flask import Flask, render_template, url_for, flash, redirect, session, request, g
from forms import RegistrationForm, LoginForm
import DatabaseCalls, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc158abb4eeeedac31b250d17e4f4bae'
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if DatabaseCalls.Register(form.school.data, form.email.data, form.student_id.data, form.password.data):
            flash(f'Account created for {form.email.data}!', 'register')
        else:
            flash(f'Email {form.email.data} already taken!', 'register')
        # return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/schedule", methods=['GET', 'POST'])
def schedule():
    form = RegistrationForm()
    if form.validate_on_submit():
        if DatabaseCalls.Register(form.school.data, form.email.data, form.student_id.data, form.password.data):
            flash(f'Account created for {form.email.data}!', 'register')
        else:
            flash(f'Email {form.email.data} already taken!', 'register')
        #return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data != '' and form.password.data != '':
            result = DatabaseCalls.getAccount(form.email.data, form.password.data)
            if result == form.email.data:
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'login')
        else:
            flash('Login Unsuccessful. You must enter a username and password', 'login')
    return render_template('login.html', title='Login', form=form)


@app.route('/pair')
def pair():
    if g.user:
        return render_template('pair.html')

    return redirect(url_for(login))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'


if __name__ == '__main__':
    app.run(debug=True)
