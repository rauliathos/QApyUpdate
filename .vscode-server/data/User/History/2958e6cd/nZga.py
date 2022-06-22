from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.

class UserCheck:
    def __init__(self, banned, ban_char, message=None):# Here we set up the class to have the banned and
    # message attributes. banned must be passed through at declaration.
        self.banned = banned
        self.ban_char = ban_char
        if not message:
            message = 'Please choose another username' # If no message chosen, then this default
            # message is returned.
        self.message = message

    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. 
    #If the data in our field is in the list of words then raise a ValidationError object with a 
    #message.
        if  (for char in self.ban_char) in field.data :
             raise ValidationError(self.message)
        if  field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one.
        # We pass through the list of banned usernames as a list.
        UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')

    def validate_username():
        ban_char= ['!','@', '$', '£','/']
        if ban_char in username :
        return "Unallowed char!!!"
         

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')