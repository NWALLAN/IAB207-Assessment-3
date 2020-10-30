from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, SelectField, FileField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    phone=IntegerField("Contact Number", validators=[InputRequired()])
    address=StringField("Shipping Address", validators=[InputRequired()])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id=StringField("Email Address", validators=[Email("Please enter a valid email")])
    phone=IntegerField("Phone Number", validators=[InputRequired("Please enter a valid phone number")])
    address=StringField("Sipping Address", validators=[InputRequired("Please enter your shipping address")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

ALLOWED_FILES={'jpg', 'png', 'JPG', 'PNG'}
class CreateItem(FlaskForm):
    product_name=StringField('Product Name', validators=[InputRequired()])
    product_description=StringField('Product Description', validators=[InputRequired()])
    product_category=SelectField('Categories', choices= [('Paintings', 'Paintings'), ('Photography', 'Photography'), ('Sculptign', 'Sculpting'), ('Calligraphy', 'Calligraphy'), ('Illustrations', 'Illustrations'), ('Printmaking', 'Printmaking'), ('Graphic Design', 'Graphic Design')])
    product_bidstart=StringField('Starting Bid Price', validators=[InputRequired()])
    product_image=FileField(validators=[FileRequired(), FileAllowed(ALLOWED_FILES)])
    submit=SubmitField("Create Listing")