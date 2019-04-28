from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import DatabaseCalls

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc158abb4eeeedac31b250d17e4f4bae'


@app.route("/")
@app.route("/home")
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
        #return redirect(url_for('home'))
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
    #confirm = DatabaseCalls()
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data != '' and form.password.data != '':
            flash(DatabaseCalls.getAccount(form.email.data, form.password.data), 'success')
            #if confirm.getAccount()
            #{{form.email(class_="flagged")}}
            #return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
