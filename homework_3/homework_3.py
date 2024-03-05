from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

from models import User, db
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'GordeySecretKey'
csrf = CSRFProtect(app)

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=16)])

@app.route('/')
def index():
    return render_template('index.html')

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')

@app.route('/registry/', methods=['GET', 'POST'])
def registry():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        db.session.add(user)
    db.session.commit()
    return render_template('registry.html', form=form)
if __name__ == '__main__':
    app.run()