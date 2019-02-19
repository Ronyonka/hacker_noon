from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Blog,Comment
from .forms import BlogForm,CommentForm
from .. import db
from ..request import get_quotes

@main.route('/')
def index():

	title = 'Home Page - Welcome to  B-Logs, your daily inspiration'

	index=Blog.query.all()
	first=Blog.query.limit(1).all()

	random_quotes = get_quotes()
	quote= random_quotes['quote']

	author= random_quotes['author']


	return render_template('index.html', title=title,author=author,quote=quote,index=index,first=first)

@main.route('/new_blog', methods = ['GET','POST'])
@login_required
def new_blog():
	form = BlogForm()
	if form.validate_on_submit():
		blog = Blog(post=form.post.data,body=form.body.data)
		blog.save_blog()
		return redirect(url_for('main.index'))
	return render_template('new_blog.html',form=form)

@main.route('/view_blogs/<int:blog_id>', methods = ['GET','POST'])
def view_blogs(blog_id):
	blog = Blog.query.filter_by(id=blog_id).first()
	first=Blog.query.limit(1).all()

	
	form = CommentForm()
	if form.validate_on_submit():
		name = form.name.data
		comment = form.comment.data
		new_comment = Comment(name=name, comment=comment,blog_id=blog.id)
		new_comment.save_comment()
		return redirect(url_for('main.view_blogs', blog_id=blog.id))
	comments = Comment.query.filter_by(blog_id=blog.id)
	return render_template('view_blogs.html',first=first,blog=blog, form=form,comments=comments)
