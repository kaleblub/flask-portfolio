from database import Base, engine, SessionLocal
from models import Post, Tag

session=SessionLocal(bind=engine)

posts = [
	{
		"title": "Test Post One",
		"summary": "This is the summary of the first post.",
		"content": "This is the content of the first post."
	},
	{
		"title": "Test Post Two",
		"summary": "This is the summary of the second post.",
		"content": "This is the content of the second post."
	},
	{
		"title": "Test Post Three",
		"summary": "This is the summary of the third post.",
		"content": "This is the content of the third post."
	},
	{
		"title": "Test Post Four",
		"summary": "This is the summary of the fourth post.",
		"content": "This is the content of the fourth post."
	},	
]

tags = [
	{
		"title": "Python",
		"content": "Python3"
	}, 
	{
		"title": "C++",
		"content": "cpp"
	},
	{
		"title": "Bash",
		"content": "sh"
	}
]

for post in posts:
	session.add(Post(title=post["title"], summary=post["summary"], content=post["content"]))

for tag in tags:
	session.add(Tag(title=tag["title"], content=tag["content"]))

session.commit()