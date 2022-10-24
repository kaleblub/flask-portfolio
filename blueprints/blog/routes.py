from flask import Blueprint, render_template, request, redirect, session
from ..models import Post
from database import SessionLocal
from static.scripts import getPostFiles, returnSeperatedData
import os
import markdown
import hashlib


blog_bp = Blueprint('blog_bp', __name__, template_folder="templates/blog")
session = SessionLocal()

# --- This Should Be Temporary Unless Superior, Using The Static Content Files ---
yearFolder = "./content/"
year_to_files_dict = getPostFiles(yearFolder)

for (year, file_list) in year_to_files_dict.items():
	for file in enumerate(file_list):
		year_to_files_dict[year][file[0]] = returnSeperatedData(yearFolder + year + '/' + file[1])


# ----------------------- Render Main Blog Page --------------------------
@blog_bp.route("/", methods=['GET'])
def blog():
	allPosts = session.query(Post).all()

	
	# Sort the posts by date
	sortedPosts = {}

	# For each post,
	# for (year, post) in year_to_files_dict: # Was staticPosts
		# If the year is not already a key in sortedPosts dict
		# print(sortedPosts.keys() == None)
		# if postYear not in sortedPosts.keys():
			# i
			# create a key of the year, and append the post
		# 	sortedPosts[postYear] = []
		# 	sortedPosts[postYear].append(post)
		# else:



		# print(post['date_created'])
	return render_template("blog.html", posts=allPosts, staticPosts=year_to_files_dict)


# ----------------------- Render Individual Posts --------------------------
# @blog_bp.route("/<int:id>")
# def postPage(id):
# 	post = session.query(Post).filter(Post.id == id).first()
# 	print(post)
# 	return render_template("posts.html", post=post)

# ---------------- Render Static Post Content -----------------
@blog_bp.route("<string:year>/<string:id>")
def staticPostPage(year, id):
	post = year_to_files_dict[year][int(id)]
	post['content'] = markdown.markdown(''.join(post['content']), extensions=['fenced_code', 'codehilite'])

	return render_template("staticPosts.html", post=post)

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