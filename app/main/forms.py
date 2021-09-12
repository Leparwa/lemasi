from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.fields.simple import FileField
from wtforms.validators import Required

class ProductForm(FlaskForm):

    title = StringField('Book Title',validators=[Required()])
    author = StringField('Book Author',validators=[Required()])
    description = TextAreaField('Book Description',validators=[Required()])
    price = StringField('Book Price',validators=[Required()])
    image =  StringField('image link')
    submit = SubmitField('Submit')