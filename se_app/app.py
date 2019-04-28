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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        session.pop('user', None)
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                session['user'] = 'admin@blog.com'
                return redirect(url_for('protected'))
#    form = LoginForm()
#    if form.validate_on_submit():
#        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#            flash('You have been logged in!', 'success')


            #{{form.email(class_="flagged")}}
            #return redirect(url_for('home'))
#        else:
#            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/protected')
def protected():
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
