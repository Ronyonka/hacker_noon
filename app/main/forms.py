from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
	name = StringField('Enter Name:',validators=[Required()])

	comment = TextAreaField('Add comment', validators=[Required()])

	submit = SubmitField('Submit')

class BlogForm(FlaskForm):
	post = StringField('Topic',validators=[Required()])
	body = TextAreaField('blog')

	submit = SubmitField('blog')