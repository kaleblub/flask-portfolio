from flask import Blueprint, render_template, request, redirect, session
from ..models import Post
from database import SessionLocal
from static.scripts import getPostFiles, returnSeperatedData
import os
import markdown
import hashlib


blog_bp = Blueprint('blog_bp', __name__, template_folder="templates/blog")
session = SessionLocal()
app_root_directory = os.getcwd()

# --- This Should Be Temporary Unless Superior, Using The Static Content Files --- 	
staticPosts = []
for file in getPostFiles():
	staticPosts.append(returnSeperatedData(file))


# ----------------------- Render Blog Page --------------------------
@blog_bp.route("/", methods=['GET'])
def blog():
	allPosts = session.query(Post).all()
	
	# # Sort the posts by date
	# sortedPosts = []
	# for post in staticPosts:
		
	# 	print(sorted(post['date_created']))
	return render_template("blog.html", posts=allPosts, staticPosts=staticPosts)


# ----------------------- Render Individual Posts --------------------------
# @blog_bp.route("/<int:id>")
# def postPage(id):
# 	post = session.query(Post).filter(Post.id == id).first()
# 	print(post)
# 	return render_template("posts.html", post=post)

# ---------------- Render Static Post Content -----------------
@blog_bp.route("/<string:id>")
def staticPostPage(id):
	post = staticPosts[int(id)]
	post['content'] = markdown.markdown(''.join(post['content']), extensions=['fenced_code', 'codehilite'])
	
	shortPath = app_root_directory + "/static/css/"
	files = os.listdir(shortPath)
	for file in files:
		files[files.index(file)] = shortPath + file

	return render_template("staticPosts.html", post=post, cssFiles=files)

# @blog_bp.route("/", methods=['GET', 'POST'])
# def posts():
# 	if request.method == 'POST':
# 		postTitle = request.form['title']
# 		postContent = request.form['content']
# 		postAuthor = request.form['author']
# 		newPost = BlogPost(title=postTitle, content=postContent, author=postAuthor)
# 		db.session.add(newPost)
# 		db.session.commit()
# 		return redirect('/blog')
# 	else:
# 		allPosts = BlogPost.query.order_by(BlogPost.id).all()
# 		return render_template("blog.html", posts=allPosts)

# # ----------------------- Delete Post Based On Which Delete Button Was Clicked --------------------------
# @blog_bp.route('/delete/<int:id>')
# def deletePost(id):
# 	post = BlogPost.query.get_or_404(id)
# 	db.session.delete(post)
# 	db.session.commit()
# 	return redirect('/blog')

# # ----------------------- Render Page To Edit Blog Post --------------------------
# @blog_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
# def editPost(id):
# 	post = BlogPost.query.get_or_404(id)
	
# 	if request.method == 'POST':
# 		post.title = request.form['title']
# 		post.author = request.form['author']
# 		post.content = request.form['content']
# 		db.session.commit()
# 		return redirect('/blog')
# 	else:
# 		return render_template("edit.html", post=post)