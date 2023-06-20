from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phoneno', validators=[DataRequired()])
    total_price = DecimalField("total_price", validators=[DataRequired()])
    submit = SubmitField("Register")




class ProductForm(FlaskForm):
    product_name = StringField('Product', validators=[DataRequired()])
    product_price = DecimalField('productPrice', validators=[DataRequired()])
    submit = SubmitField("Submit")




