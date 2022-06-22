from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth= DateField('Date of Birth')
    fav_num = IntegerField('Favorite Number', size=2)
    fav_food = SelectField('Favorite Food', choices=[
        ('pizza', 'Pizza'), 
        ('spaghetti', 'Spaghetti'),
         ('chilli', 'Chilli')
    ])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
       # date_of_birth = form.date_of_birth.data
       # fav_num = form.fav_num.data
        #fav_food = form.fav_food.data


        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')