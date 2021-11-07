from database import Base, engine, SessionLocal
from models import Post, Tag, User, LikesOnComment, LikesOnPost, Comment, Project, Category, PostTagAssociation, ProjectCategoryAssociation 

session=SessionLocal(bind=engine)

users = [
	{
		"name": "Kaleb Humpal",
		"email": "kaleblub@gmail.com",
		"date_registered": "",
		"last_login": "",
		"status": True,
		
	}, 
]

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
	}, 
	{
		"title": "C++",
	},
	{
		"title": "Bash",
	}
]

categories = [
	{
		'title': 'Python',
	},
	{
		'title': 'C++',
	},
	{
		'title': 'HTML',
	},
	{
		'title': 'CSS',
	},
	{
		'title': 'SCSS',
	},
	{
		'title': 'Bash',
	},
	{
		'title': 'JavaScript',
	},

]

projects = [
	{
		"title": "Pygame-Tetris",
		"summary": "Pygame version of the classic game Tetris. In this project, I crafted a fully functional menu, highscore, controls, and gameover screens. I also made a highscore system with pickle.",
		"status": True,
		"date_created": "2021-8-4",
		"thumbnail_image": '../../static/img/tetris.png',
	},
	{
		"title": "Freerice-Bot",
		"summary": "A python web-scraping bot to play quiz games on the website www.freerice.com and donate rice automatically. It is made with Python's Selenium and has modules for vocabulary, basic multiplication, etc.",
		"status": True,
		"date_created": '2019-11-20',
		"thumbnail_image": '',
	},
	{
		"title": "Flask-Portfolio",
		"summary": "This is my personal project of building my own Flask portfolio website. I have an about me page, a blog, my portfolio page showing my projects and a contact modal.",
		"status": True,
		"date_created": '2021-11-2',
		"thumbnail_image": ,
	},
	{
		"title": "Pygame-Space-Invaders",
		"summary": "Space Invaders made with Python's Pygame library.",
		"status": False,
		"date_created": ,
		"thumbnail_image": ,
	},
	{
		"title": "Pygame-Pong",
		"summary": "Basic Pong clone made with Python's Pygame library.",
		"status": False,
		"date_created": ,
		"thumbnail_image": '../../static/img/pong.png',
	},
	{
		"title": "Pygame-TicTacToe",
		"summary": "This is my first Pygame project, a simple rendition of TicTacToe with python.",
		"status": False,
		"date_created": "2021-7-24",
		"thumbnail_image": '../../static/img/TicTacToe.png',
	},
]

for post in posts:
	session.add(Post(title=post["title"], summary=post["summary"], content=post["content"]))

for tag in tags:
	session.add(Tag(title=tag["title"], content=tag["content"]))

session.commit()