from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship, backref

# Import The Declarative Base 
from database import Base

class BlogPost(Base):
	__tablename__ = "posts"
	
	id = Column(Integer, primary_key=True)
	title = Column(String(50), nullable=False, unique=True)
	summary = Column(String(200), nullable=False)
	dateCreated = Column(DateTime, default=datetime.utcnow())
	content = Column(Text, nullable=False)
	author = Column(String, default="Kaleb Humpal")
	tags = Column(String, nullable=True)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'summary': self.summary,
			'dateCreated': self.dateCreated,
			'content': self.content,
			'author': self.author,
		}