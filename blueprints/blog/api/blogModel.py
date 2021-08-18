from api import db
from datetime import datetime
from api.Tags_Blog.tag_blog_table import tag_blog

class BlogPosts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(Integer, )
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'content'
		}

# ----------------------- Blog Post Database Model --------------------------
class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(30), nullable=False, default="N/A")
	datePosted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return 'Blog post ' + str(self.id)