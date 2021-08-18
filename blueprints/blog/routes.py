from flask import Blueprint, render_template, request, redirect

blog_bp = Blueprint('blog_bp', __name__, template_folder="templates/blog")

# ----------------------- Render Blog Page --------------------------
@blog_bp.route("/", methods=['GET', 'POST'])
def posts():
	if request.method == 'POST':
		postTitle = request.form['title']
		postContent = request.form['content']
		postAuthor = request.form['author']
		newPost = BlogPost(title=postTitle, content=postContent, author=postAuthor)
		db.session.add(newPost)
		db.session.commit()
		return redirect('/blog')
	else:
		allPosts = BlogPost.query.order_by(BlogPost.id).all()
		return render_template("blog.html", posts=allPosts)

# ----------------------- Delete Post Based On Which Delete Button Was Clicked --------------------------
@blog_bp.route('/delete/<int:id>')
def deletePost(id):
	post = BlogPost.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()
	return redirect('/blog')

# ----------------------- Render Page To Edit Blog Post --------------------------
@blog_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def editPost(id):
	post = BlogPost.query.get_or_404(id)
	
	if request.method == 'POST':
		post.title = request.form['title']
		post.author = request.form['author']
		post.content = request.form['content']
		db.session.commit()
		return redirect('/blog')
	else:
		return render_template("edit.html", post=post)