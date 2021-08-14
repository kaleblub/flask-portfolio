from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# ----------------------- Projects Database Model --------------------------
# class ProjectPost(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(100), nullable=False)
# 	content = db.Column(db.Text, nullable=False)



# ----------------------- Blog Post Database Model --------------------------
class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(30), nullable=False, default="N/A")
	datePosted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return 'Blog post ' + str(self.id)


# ----------------------- Render Home Page --------------------------
@app.route('/')
def home():
	return render_template("index.html")


# ----------------------- Render About Page --------------------------
@app.route('/about')
def about():
	return render_template("about.html")


# ----------------------- Render Projects Page --------------------------
@app.route('/projects')
def projects():
	return render_template("projects.html") #, projects=allProjects)

# ----------------------- Render Blog Page --------------------------
@app.route("/posts", methods=['GET', 'POST'])
def posts():
	if request.method == 'POST':
		postTitle = request.form['title']
		postContent = request.form['content']
		postAuthor = request.form['author']
		newPost = BlogPost(title=postTitle, content=postContent, author=postAuthor)
		db.session.add(newPost)
		db.session.commit()
		return redirect('/posts')
	else:
		allPosts = BlogPost.query.order_by(BlogPost.id).all()
		return render_template("posts.html", posts=allPosts)

# ----------------------- Delete Post Based On Which Delete Button Was Clicked --------------------------
@app.route('/posts/delete/<int:id>')
def deletePost(id):
	post = BlogPost.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()
	return redirect('/posts')

# ----------------------- Render Page To Edit Blog Post --------------------------
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def editPost(id):
	post = BlogPost.query.get_or_404(id)
	
	if request.method == 'POST':
		post.title = request.form['title']
		post.author = request.form['author']
		post.content = request.form['content']
		db.session.commit()
		return redirect('/posts')
	else:
		return render_template("edit.html", post=post)

# @app.route("/403")
# def error_403():
# 	return '', 403

if __name__ == "__main__":
	app.run(debug=True)