from sqlalchemy import Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship, backref
from datetime import datetime

# Import The Declarative Base & The Engine
from database import Base, engine
from static.scripts import getWordCount

PostTagAssociation = Table('PostTagAssociations', Base.metadata,
	Column('postId', ForeignKey('posts.id')),
	Column('tagId', ForeignKey('tags.id'))
)

class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True)
	title = Column(String(50), nullable=False, unique=True)
	author = Column(String(50), nullable=False, default="Kaleb Humpal")
	summary = Column(String(200), nullable=False)
	# status = Column(Boolean, nullable=False) # True or False if the post is posted
	date_created = Column(DateTime, default=datetime.utcnow())
	content = Column(Text, nullable=False)
	# authorId = Column(Integer, ForeignKey('users.id'))
	# comments = relationship("Comments", backref=backref("posts", uselist=True))
	tags = relationship("Tag", secondary=PostTagAssociation)
	# likes = relationship("LikesOnPosts")
	word_count = Column(Integer)

	def __repr__(self):
		return "<Post(id='%s', title='%s', author='%s', summary='%s', date_created='%s', word_count='%s')>" \
			% (self.id, self.title, self.author, self.summary, self.date_created, self.word_count)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'author': self.author,
			'tags': self.tags,
			'summary': self.summary,
			'date_created': self.dateCreated,
			'content': self.content,
			'word_count': getWordCount(self.content)
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


# Run This File Alone To Create 
# The Database With The Table Models Above
if __name__ == "__main__":
	Base.metadata.create_all(engine)