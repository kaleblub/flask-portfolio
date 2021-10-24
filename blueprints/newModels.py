from sqlalchemy import Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship, backref
from datetime import datetime

# Import The Declarative Base 
from database import Base, engine


class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(50), nullable=False)
	email = Column(String(50), nullable=False, unique=True)
	dateRegistered = Column(DateTime, default=datetime.utcnow())
	lastLogin = Column(DateTime)
	userStatus = Column(Boolean, nullable=False) # True or False if the user is Admin
	posts = relationship("Posts") # One to many reference to Posts table
	comments = relationship("Comments") # One to many reference to Comments table
	commentLikes = relationship("LikesOnComments")
	postLikes = relationship("LikesOnPosts")

	def __repr__(self):
		return "<User()>" % ()

	# @property
	# def serialize(self):
	# 	return {
	# 		'id': self.id,
	# 		'name': self.name,
	# 		'email': self.email,
	# 		'dateRegistered': self.dateRegistered,
	# 		'lastLogin': self.lastLogin,
	# 		'userStatus': self.userStatus,
	# 	}

class LikesOnComment(Base):
	__tablename__ = 'LikesOnComments'
	id = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey('users.id'))
	commentsId = Column(Integer, ForeignKey('comments.id'))
	likeOrDislike = Column(Boolean, nullable=True)

	def __repr__(self):
		return "<LikesOnComments>"

class LikesOnPost(Base):
	__tablename__ = 'LikesOnPosts'
	id = Column(Integer, primary_key=True)
	userId = Column(Integer, ForeignKey('users.id'))
	postsId = Column(Integer, ForeignKey('posts.id'))
	likeOrDislike = Column(Boolean, nullable=True)

# LikesOnComments = Table('LikesOnComments', Base.metadata,
# 	Column(Integer, primary_key=True),
# 	Column('userId', Integer, ForeignKey('users.id')),
# 	Column('commentsId', Integer, ForeignKey('comments.id'))
# )

# LikesOnPosts = Table('LikesOnPosts', Base.metadata,
# 	Column(Integer, primary_key=True),
# 	Column('userId', Integer, ForeignKey('users.id')),
# 	Column('postId', Integer, ForeignKey('posts.id'))
# )
	

class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True)
	title = Column(String(50), nullable=False, unique=True)
	summary = Column(String(200), nullable=False)
	status = Column(Boolean, nullable=False) # True or False if the post is posted
	dateCreated = Column(DateTime, default=datetime.utcnow())
	content = Column(Text, nullable=False)
	authorId = Column(Integer, ForeignKey('users.id'))
	comments = relationship("Comments", backref=backref("posts", uselist=True))
	tags = relationship("Tag", secondary=PostTagAssociation)
	likes = relationship("LikesOnPosts")
	word_count = getWordCount()

	def getWordCount(self):
		contentWordList = self.content.split(" ")
	    wordCount = 0
	    for word in content:
	        wordCount += 1
	    return wordCount

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'summary': self.summary,
			'status': self.status,
			'dateCreated': self.dateCreated,
			'content': self.content,
			'authorId': self.authorId,
		}

class Comment(Base):
	__tablename__ = "comments"
	id = Column(Integer, primary_key=True) # ID of the comment
	title = Column(String(50), nullable=False) # Title of Comment
	status = Column(Boolean, nullable=False) # True or False if the comment is allowed or not
	dateCreated = Column(DateTime, default=datetime.utcnow) # Date the Comment was posted
	content = Column(Text, nullable=False) # The text of the comment
	postId = Column(Integer, ForeignKey('posts.id'), nullable=False) # ID of the Parent Post of the Comment
	authorId = Column(Integer, ForeignKey('users.id'), nullable=False) # ID of the User who posted the comment
	parentCommentId = Column(Integer, ForeignKey('comments.id'), nullable=True )
	parentComment = relationship('Comments')
	likes = relationship("LikesOnComments")

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'status': self.status,
			'dateCreated': self.status,
			'content': self.content,
			'postId': self.postId,
			'authorId': self.authorId,
			'parentCommentId': self.parentCommentId,
		}

class Tag(Base):
	__tablename__ = "tags"
	id = Column(Integer, primary_key=True)
	title = Column(String(20), nullable=False)
	content = Column(String(20), nullable=False)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'content': self.content,
		}

# class PostTagAssociation(Base):
# 	__tablename__ = 'PostTagAssociations'
# 	id = Column(Integer, primary_key=True)
# 	postId = Column(Integer, ForeignKey('posts.id'))
# 	tagId = Column(Integer, ForeignKey('tags.id'))

PostTagAssociation = Table('PostTagAssociations', Base.metadata,
	Column('postId', ForeignKey('posts.id')),
	Column('tagId', ForeignKey('tags.id'))
)

class Categories(Base):
	__tablename__ = "categories"
	id = Column(Integer, primary_key=True)
	title = Column(String(50), nullable=False)
	content = Column(String(50), nullable=False)
	icon = Column(String(50), nullable=False) # Icon of the Language/Tool used in the project

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'content': self.content,
			'icon': self.icon,
		}

ProjectCategoryAssociation = Table('projectCategory', Base.metadata,
	Column('projectId', Integer, ForeignKey('projects.id')),
	Column('categoryId', Integer, ForeignKey('categories.id'))
)

class Projects(Base):
	__tablename__ = "projects"
	id = Column(Integer, primary_key=True)
	title = Column(String(50), nullable=False)
	summary = Column(String(200), nullable=False)
	status = Column(Integer)
	dateCreated = Column(DateTime, default=datetime.utcnow)
	thumbnailImage = Column(String(250))
	authorId = Column(Integer, ForeignKey('users.id'), nullable=False)
	categories = relationship("Categories", secondary=ProjectCategoryAssociation)

if __name__ == "__main__":
	Base.metadata.create_all(engine)